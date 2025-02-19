from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import logging
import os
import pandas as pd
import csv

app = Flask(_name_)
logging.basicConfig(level=logging.INFO)

BASE_URL = "https://www.vlr.gg"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

@app.route("/search_player", methods=["GET"])
def search_player():
    player_name = request.args.get("player_name")
    if not player_name:
        return jsonify({"error": "Player name is required"}), 400

    search_url = f"{BASE_URL}/search/?q={player_name.replace(' ', '%20')}&type=players"
    response = requests.get(search_url, headers=HEADERS)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data"}), 500

    soup = BeautifulSoup(response.content, 'html.parser')
    player_link = soup.find('a', class_='search-item')
    if player_link:
        return jsonify({"profile_url": BASE_URL + player_link['href']})
    else:
        return jsonify({"error": "Player not found"}), 404

@app.route("/get_player_stats", methods=["GET"])
def get_player_stats():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Player profile URL is required"}), 400

    response = requests.get(url, headers=HEADERS)
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
                    stats.append({
                        'Agent': agent_name,
                        'Usage': cells[1].text.strip(),
                        'Rounds Played': cells[2].text.strip(),
                        'Rating': cells[3].text.strip(),
                        'ACS': cells[4].text.strip(),
                        'K:D': cells[5].text.strip(),
                        'ADR': cells[6].text.strip(),
                        'KAST': cells[7].text.strip(),
                        'KPR': cells[8].text.strip(),
                        'APR': cells[9].text.strip(),
                        'First Kills Per Round': cells[10].text.strip(),
                        'First Deaths Per Round': cells[11].text.strip(),
                        'Kills': cells[12].text.strip(),
                        'Deaths': cells[13].text.strip(),
                        'Assists': cells[14].text.strip(),
                        'First Kills': cells[15].text.strip(),
                        'First Deaths': cells[16].text.strip()
                    })
            return jsonify({'Name': name, 'Stats': stats})
        except Exception as e:
            logging.error(f"Error processing player {name}: {str(e)}")
            return jsonify({"error": "Failed to process data"}), 500
    else:
        return jsonify({"error": "Stats table not found"}), 404

@app.route("/analyze_players", methods=["GET"])
def analyze_players():
    files = [f for f in os.listdir() if f.endswith(".csv") and f != "all_players_stats.csv"]
    if not files:
        return jsonify({"error": "No player CSV files found"}), 404

    all_data = []
    for file in files:
        df = pd.read_csv(file)
        player_name = file.replace(".csv", "").replace("_", " ")
        avg_acs = df["ACS"].astype(float).mean()
        avg_adr = df["ADR"].astype(float).mean()
        avg_kd = df["K:D"].astype(float).mean()
        avg_kast = df["KAST"].str.replace('%', '').astype(float).mean()
        success_score = round((avg_acs * 0.4 + avg_kd * 0.3 + avg_adr * 0.2 + avg_kast * 0.1), 2)
        all_data.append({
            "Player": player_name,
            "Avg ACS": avg_acs,
            "Avg ADR": avg_adr,
            "Avg K:D": avg_kd,
            "Avg KAST": avg_kast,
            "Success Score": success_score
        })
    return jsonify(all_data)

if _name_ == "_main_":
    app.run(debug=True)