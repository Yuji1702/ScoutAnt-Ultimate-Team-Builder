import pandas as pd
import os
import csv

# Step 1: Define agent roles in Valorant
AGENT_ROLES = {
    # 🌫️ Controllers
    "Brimstone": "Controller", "Viper": "Controller", "Omen": "Controller",
    "Astra": "Controller", "Harbor": "Controller", "Clove": "Controller",

    # 🎯 Initiators
    "Sova": "Initiator", "Breach": "Initiator", "Skye": "Initiator", "KAY/O": "Initiator",
    "Fade": "Initiator", "Gekko": "Initiator", "Tejo": "Initiator",

    # 🛡️ Sentinels
    "Killjoy": "Sentinel", "Cypher": "Sentinel", "Sage": "Sentinel",
    "Chamber": "Sentinel", "Deadlock": "Sentinel", "Vyse": "Sentinel",

    # 🔥 Duelists
    "Phoenix": "Duelist", "Jett": "Duelist", "Reyna": "Duelist", "Raze": "Duelist",
    "Yoru": "Duelist", "Neon": "Duelist", "Iso": "Duelist"
}

# Step 2: Function to read CSV file and process player stats
def analyze_player_performance(file_path):
    """Reads a player's CSV file, categorizes agent roles, and calculates performance metrics."""
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return None

    df = pd.read_csv(file_path)

    # Initialize role-based data storage
    role_stats = {role: {"Rounds": 0, "ACS": 0, "ADR": 0, "K:D": 0, "KAST": 0, "Count": 0} for role in set(AGENT_ROLES.values())}

    # Step 3: Categorize each agent into their respective roles
    for _, row in df.iterrows():
        agent = row["Agent"]
        role = AGENT_ROLES.get(agent, "Unknown")

        if role != "Unknown":
            role_stats[role]["Rounds"] += int(row["Rounds Played"])
            role_stats[role]["ACS"] += float(row["ACS"])
            role_stats[role]["ADR"] += float(row["ADR"])
            role_stats[role]["K:D"] += float(row["K:D"])
            role_stats[role]["KAST"] += float(row["KAST"].replace('%', ''))  # Remove % and convert to float
            role_stats[role]["Count"] += 1  # Track number of agents per role

    # Step 4: Calculate the average success per role
    role_performance = []
    for role, stats in role_stats.items():
        if stats["Count"] > 0:
            avg_acs = round(stats["ACS"] / stats["Count"], 2)
            avg_adr = round(stats["ADR"] / stats["Count"], 2)
            avg_kd = round(stats["K:D"] / stats["Count"], 2)
            avg_kast = round(stats["KAST"] / stats["Count"], 2)
            success_score = round((avg_acs * 0.4 + avg_kd * 0.3 + avg_adr * 0.2 + avg_kast * 0.1), 2)  # Weighted metric
            
            role_performance.append([role, stats["Rounds"], avg_acs, avg_adr, avg_kd, avg_kast, success_score])

    return role_performance

# Step 5: Function to analyze all players (single or multiple files)
def analyze_all_players():
    """Analyzes all player CSV files and generates a success report."""
    files = [f for f in os.listdir() if f.endswith(".csv") and f != "all_players_stats.csv"]

    if not files:
        print("❌ No player CSV files found!")
        return

    print(f"🔍 Found {len(files)} player files: {files}")

    all_data = []
    for file in files:
        print(f"\n🔍 Analyzing {file} ...")
        player_performance = analyze_player_performance(file)

        if player_performance:
            player_name = file.replace(".csv", "").replace("_", " ")
            for row in player_performance:
                all_data.append([player_name] + row)
        else:
            print(f"⚠️ No valid data found in {file}.")

    if not all_data:
        print("❌ No valid player performance data found. Exiting.")
        return
    
    # Step 6: Save results to CSV
    output_file = "player_role_analysis.csv"
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Player", "Role", "Total Rounds", "Avg ACS", "Avg ADR", "Avg K:D", "Avg KAST", "Success Score"])
        writer.writerows(all_data)

    print(f"\n✅ Analysis complete! Results saved to {output_file}")


# Run analysis
if __name__ == "__main__":
    analyze_all_players()
