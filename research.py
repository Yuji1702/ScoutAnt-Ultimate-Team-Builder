import requests
from bs4 import BeautifulSoup
import time
import random
import logging
import csv
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict

logging.basicConfig(level=logging.INFO)

class ValorantDataCollector:
    def __init__(self):
        self.base_url = "https://www.vlr.gg"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def search_player(self, player_name: str) -> str:
        """Search for a player by name and return their profile URL."""
        search_url = f"{self.base_url}/search/?q={player_name.replace(' ', '%20')}&type=players"
        response = requests.get(search_url, headers=self.headers)

        if response.status_code != 200:
            logging.error(f"Failed to retrieve search page for {player_name}")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        player_link = soup.find('a', class_='search-item')

        if player_link:
            return self.base_url + player_link['href']
        else:
            logging.warning(f"Player {player_name} not found.")
            return None

    def get_player_stats(self, url: str) -> Dict:
        """Extract stats for a single player, replacing missing values with '0'."""
        url_with_timespan = f"{url}?timespan=all"
        response = requests.get(url_with_timespan, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        name_tag = soup.find('h1', class_='wf-title')
        name = name_tag.text.strip() if name_tag else 'Unknown'

        stats_table = soup.find('table', class_='wf-table')
        stats = []

        if stats_table:
            try:
                stats_rows = stats_table.find('tbody').find_all('tr')
                for row in stats_rows:
                    cells = row.find_all('td')
                    if len(cells) >= 2:
                        agent_img = cells[0].find('img')
                        agent_name = agent_img['alt'] if agent_img else 'Unknown'

                        # Handling missing values
                        def safe_text(cell):
                            return cell.text.strip() if cell and cell.text.strip() else "0"

                        stats.append({
                            'Agent': agent_name,
                            'Usage': safe_text(cells[1]),
                            'Rounds Played': safe_text(cells[2]),
                            'Rating': safe_text(cells[3]),
                            'ACS': safe_text(cells[4]),
                            'K:D': safe_text(cells[5]),
                            'ADR': safe_text(cells[6]),
                            'KAST': safe_text(cells[7]),
                            'KPR': safe_text(cells[8]),
                            'APR': safe_text(cells[9]),
                            'First Kills Per Round': safe_text(cells[10]),
                            'First Deaths Per Round': safe_text(cells[11]),
                            'Kills': safe_text(cells[12]),
                            'Deaths': safe_text(cells[13]),
                            'Assists': safe_text(cells[14]),
                            'First Kills': safe_text(cells[15]),
                            'First Deaths': safe_text(cells[16])
                        })

                return {'Name': name, 'Stats': stats}

            except Exception as e:
                logging.error(f"Error processing player {name}: {str(e)}")
                return None
        else:
            logging.warning(f"Stats table not found for player: {name}")
            return None


def export_player_stats(player_data, filename):
    """Exports player stats to CSV."""
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow([
                'Name', 'Agent', 'Usage', 'Rounds Played', 'Rating', 'ACS', 'K:D',
                'ADR', 'KAST', 'KPR', 'APR', 'First Kills Per Round', 'First Deaths Per Round',
                'Kills', 'Deaths', 'Assists', 'First Kills', 'First Deaths'
            ])

        for stat in player_data['Stats']:
            writer.writerow([
                player_data['Name'],
                stat['Agent'],
                stat['Usage'],
                stat['Rounds Played'],
                stat['Rating'],
                stat['ACS'],
                stat['K:D'],
                stat['ADR'],
                stat['KAST'],
                stat['KPR'],
                stat['APR'],
                stat['First Kills Per Round'],
                stat['First Deaths Per Round'],
                stat['Kills'],
                stat['Deaths'],
                stat['Assists'],
                stat['First Kills'],
                stat['First Deaths']
            ])


def collect_data_for_player(player_name, collector, concurrent):
    """Collects data for a single player and saves it accordingly."""
    player_url = collector.search_player(player_name)
    if player_url:
        player_stats = collector.get_player_stats(player_url)
        if player_stats:
            if concurrent:
                export_player_stats(player_stats, 'all_players_stats.csv')
            else:
                filename = f"{player_stats['Name'].replace(' ', '_')}.csv"
                export_player_stats(player_stats, filename)


def collect_and_save_data(player_names: List[str], concurrent=False):
    """Collects data for multiple players and saves to CSV."""
    collector = ValorantDataCollector()

    logging.info(f"Collecting data for {len(player_names)} players...")
    print(f"DEBUG: collect_and_save_data received concurrent={concurrent}")

    if concurrent:
        logging.info("Running in concurrent mode... (Single File)")
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(collect_data_for_player, player_name, collector, concurrent) for player_name in player_names]
            for future in futures:
                future.result()
    else:
        logging.info("Running in sequential mode... (Separate Files)")
        for player_name in player_names:
            collect_data_for_player(player_name, collector, concurrent)
            time.sleep(random.uniform(1.5, 3.0))  # Politeness delay

    logging.info("Data collection completed.")


if __name__ == "__main__":
    try:
        player_names = input("Enter the player names (comma-separated): ").split(',')
        player_names = [name.strip() for name in player_names]

        concurrent_input = input("Do you want to scrape concurrently? (y/n): ").strip().lower()
        concurrent = concurrent_input == 'y'

        collect_and_save_data(player_names, concurrent=concurrent)

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
