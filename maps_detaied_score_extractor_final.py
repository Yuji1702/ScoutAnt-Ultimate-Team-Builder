import requests
from bs4 import BeautifulSoup

def extract_map_data_detailed_page_attempt_29(page_source): # Function name updated to Attempt 29
    soup = BeautifulSoup(page_source, 'html.parser')

    map_data = []

    # --- Extract Team Names (Using .team-name selector) ---
    team_name_elements = soup.select('.team-name') # Use .team-name selector - Based on HTML inspect
    team1_name = "T1" # Default if not found
    team2_name = "Team 2" # Default if not found

    if len(team_name_elements) >= 2: # Assuming first two .team-name elements are team names
        team1_name = team_name_elements[0].text.strip()
        team2_name = team_name_elements[1].text.strip()
        print(f"Debug: Extracted Team Names (using .team-name) - Team 1: '{team1_name}', Team 2: '{team2_name}'") # Debug print of team names (SUCCESS)
    else:
        print("Debug: Could not extract team names using .team-name, using defaults (T1, Team 2)") # Debug (FAILURE with .team-name)
        # Fallback to defaults (T1, Team 2) - already set


    # Select all map navigation items (map names)
    map_items = soup.select('.vm-stats-gamesnav-item.js-map-switch')

    # Select all score elements
    score_elements = soup.select('.score')

    print(f"Debug: Found {len(map_items)} map navigation items.")
    print(f"Debug: Found {len(score_elements)} score elements.")

    # Extract map names correctly (attempt to remove prefixes)
    map_names = []
    for nav_item in map_items:
        map_name_element = nav_item.find(string=lambda text: text and text.strip() and text.strip().isalpha()) # Try to find alphabetic text first
        if map_name_element:
            map_name = map_name_element.strip()
        else: # Fallback to get_text and clean up if find fails
            map_name = nav_item.get_text(strip=True)
            map_name = map_name.lstrip('0123456789').strip() # Remove leading digits and strip again
            if not map_name: # If still empty after cleanup, or original get_text was empty
                map_name = "Map Name Not Found"


        if map_name != "All Maps": # *** Condition: Skip "All Maps" tab ***
            if map_name != "Map Name Not Found": # Also skip if map name is still "Not Found" after cleanup
                map_names.append(map_name) # Append only if it's a specific map AND has a valid name
                print(f"Debug: Processing map: {map_name}") # Debug: Indicate processing of map
            else:
                print(f"Debug: Skipping map with name 'Map Name Not Found' after cleanup") # Debug skip cleaned up "Not Found"
        else:
            print(f"Debug: Skipping Overview tab (All Maps)") # Debug: Indicate skipping Overview


    print(f"Debug: Valid map names to process: {map_names}") # Debug: Valid map names after filtering

    # Extract scores correctly (same as Attempt 23)
    scores = [score.text.strip() for score in score_elements]
    print(f"Debug: Extracted scores: {scores}")

    # Ensure we have a proper match of maps to scores (for VALID maps only)
    for i in range(len(map_names)): # Loop through VALID map names only
        score_team1 = scores[i * 2] if i * 2 < len(scores) else f"Score Not Found ({team1_name})" # Use team1_name in "Not Found" message
        score_team2 = scores[i * 2 + 1] if i * 2 < len(scores) else f"Score Not Found ({team2_name})" # Use team2_name in "Not Found" message


        map_data.append({
            'map_name': map_names[i],
            team1_name: score_team1, # Use team1_name as key
            team2_name: score_team2  # Use team2_name as key
        })

    return map_data


# Testing
if __name__ == "__main__":
    detailed_page_source_code = """
<!DOCTYPE html>
<html lang="en"> 
	<head>
		<title>
			T1 vs. Team Vitality | Champions Tour 2025: Masters Bangkok | Playoffs | Valorant match | VLR.gg		</title>

					<meta name="description" content="Stats, score, streams, and VODs from T1 vs. Team Vitality - Lower Round 1 match of Champions Tour 2025: Masters Bangkok Valorant event">
				<meta charset="utf-8">

		<meta property="og:title" content="T1 vs. Team Vitality | Champions Tour 2025: Masters Bangkok | Playoffs | Valorant match | VLR.gg">
		<meta property="og:site_name" content="VLR.gg">

					<meta property="og:description" content="Stats, score, streams, and VODs from T1 vs. Team Vitality - Lower Round 1 match of Champions Tour 2025: Masters Bangkok Valorant event">
		
					
							<meta property="og:image" content="/img/vlr/favicon.png">
					
					<meta name="twitter:card" content="summary">
		
					<meta name="twitter:site" content="@vlrdotgg">
		
		<meta name="twitter:title" content="T1 vs. Team Vitality | Champions Tour 2025: Masters Bangkok | Playoffs | Valorant match | VLR.gg">

					<meta name="twitter:description" content="Stats, score, streams, and VODs from T1 vs. Team Vitality - Lower Round 1 match of Champions Tour 2025: Masters Bangkok Valorant event">
		
					
							<meta name="twitter:image" content="https://www.vlr.gg/img/vlr/logo_tw.png">
							
		<meta name="theme-color" content="#000">
		<meta name="msapplication-navbutton-color" content="#000">
		<meta name="apple-mobile-web-app-status-bar-style" content="#000">

		<link rel="preconnect" href="https://fonts.googleapis.com">
		<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
		<link href='https://fonts.googleapis.com/css?family=Roboto:400,400italic,300,700,500' rel='stylesheet' type='text/css'>
		<link rel="stylesheet" href="/css/base/main.css?v=39" type="text/css">

					
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<link rel="stylesheet" href="/css/base/r.css?v=27" type="text/css">
			
				
					
							<link rel="stylesheet" href="/css/base/pages/match.css?v=63" type="text/css">
						
					
							<link rel="stylesheet" href="/css/base/pages/match_vlr.css?v=14" type="text/css">
						
					
							<link rel="stylesheet" href="/css/base/pages/r/match.css?v=18" type="text/css">
						
					
							<link rel="stylesheet" href="/css/base/pages/thread.css?v=6" type="text/css">
						
					
							<link rel="stylesheet" href="/css/base/pages/r/thread.css?v=3" type="text/css">
						
		
					<link rel="stylesheet" class="darkmode" href="/css/base/pages/dark.css?v=51" type="text/css">
		
				
				
		
					<link rel="icon" type="image/png" href="/img/vlr/logo_lt.png">
		
		
					<link rel="canonical" href="https://www.vlr.gg/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1">
		
		<script async src="https://www.googletagmanager.com/gtag/js?id=G-XG53CMV532"></script>
		<script>
			window.dataLayer = window.dataLayer || [];
			function gtag(){dataLayer.push(arguments);}
			gtag('js', new Date());

							gtag('config', 'G-XG53CMV532', {

				'content_group':'match'

				});
					</script>

		<script type="text/javascript">
window['nitroAds'] = window['nitroAds'] || { createAd: function () { window.nitroAds.queue.push(["createAd", arguments]) }, queue: [] };
</script>
<script async src="https://s.nitropay.com/ads-823.js"></script>	</head>

		
	<body data-ctrl="thread" class="ui-color-dark  ">

	
	<header class="header">
	<nav class="header-inner">
		<div class="header-shadow"></div>
		<div class="header-div mod-first"></div>
		<a href="/" class="header-logo">
			
							<img class="header-logo-logo" src="/img/vlr/logo_header.png" style="height: 36px;">
					</a>
		<div class="header-search">
			<form action="/search/" method="get">
				<input type="search" name="q" spellcheck=false autocomplete=off placeholder="Search...">
			</form>
		</div>

		<div class="header-div mod-forums"></div>
		<a href="/threads" class="header-nav-item mod-forums mod-vlr ">
			Forums
		</a>
		
		<div class="header-div mod-matches"></div>
		<a href="/matches" class="header-nav-item mod-matches mod-vlr ">
			Matches
		</a>

		<div class="header-div mod-events"></div>
		<a href="/events" class="header-nav-item mod-events mod-vlr ">
			Events
		</a>

		<div class="header-div mod-rankings"></div>

		<a href="/rankings" class="header-nav-item mod-rankings mod-vlr ">
			Rankings

							<span style="background: #da626c; position: absolute; top: 6px; right: 6px; display: inline-block; padding: 2px 3px; border-radius: 2px; line-height: 1; height: auto; font-size: 9px; color: #f8f8f8; font-weight: 400;">
				 	BETA2
				</span>
					</a>


					<div class="header-div mod-stats"></div>
			<a href="/stats" class="header-nav-item mod-stats mod-vlr " style="position: relative;">
				Stats
			</a>
				
				
		<div class="header-div"></div>

					<div class="header-nav-item mod-vlr-spacing" style="width: 150px;"></div>
			<div class="header-div mod-vlr-spacing"></div>
		


		<div class="header-switch js-dark-switch mod-active">
			<div style="text-align: center;">
				<div style="margin-bottom: 4px;">
					<i class="fa fa-moon-o"></i>Night:
				</div>
				<span class="on">
					ON
				</span>
				<span class="off">
					OFF
				</span>
			</div>
		</div>

		<div class="header-div mod-switch"></div>

		<div class="header-switch js-spoiler-switch mod-active">
			<div style="text-align: center; ">
				<div style="margin-bottom: 4px;">
					<i class="fa fa-exclamation"></i>Spoilers:
				</div>
				<span class="on">
					ON
				</span>
				<span class="off">
					HIDDEN
				</span>
			</div>
		</div>
		<div class="header-div mod-switch"></div>
		
		<a href="/search" class="header-nav-item mod-search mod-solo">
			<i class="fa fa-search"></i>
		</a>
		<div class="header-div mod-search">
		</div>
		
		
			<a href="/user/yuji1804" class="header-nav-item mod-user mod-solo ">
				<i class="fa fa-user"></i>
			</a>
			<div class="header-div mod-user"></div>
			
			<a id="user-inbox" href="/inbox" class="header-nav-item mod-inbox mod-solo  
				">

				<i class="fa fa-envelope"></i> 
							</a>
			<div class="header-div mod-inbox"></div>

		
		<div class="header-nav-item mod-solo mod-dropdown ">
			<i class="fa fa-bars"></i>
		</div>

		<div class="header-div mod-last"></div>


		<div class="header-menu">
			<div class="header-menu-scroll">

			<a href="/events" class="header-menu-item mod-mobile mod-events">Events</a>
			<a href="/rankings" class="header-menu-item mod-mobile mod-rankings">Rankings</a>
			<a href="/stats" class="header-menu-item mod-mobile mod-stats">Stats</a>
			
						
		

			<div class="header-menu-switch js-dark-switch mod-active">
				Night:
				<span class="on">
					ON
				</span>
				<span class="off">
					OFF
				</span>
			</div>

			<div class="header-menu-switch js-spoiler-switch mod-active">
				Spoilers:
				<span class="on">
					ON
				</span>
				<span class="off">
					HIDDEN
				</span>
			</div>
	

							<a href="/user/yuji1804" class="header-menu-item"><i class="fa fa-user"></i> Profile</a>
				<a href="/inbox" class="header-menu-item" class="header-menu-item"><i class="fa fa-envelope"></i> Inbox</a>
				<a href="/settings" class="header-menu-item"><i class="fa fa-cog"></i> Settings</a>

				<a href="/auth/logout" class="logout header-menu-item"><i class="fa fa-sign-out"></i> Log out</a>
						</div>
		</div>
	</nav>
</header>

		<div id="float-left-300"></div>
	<div id="float-left-160"></div>
			<script type="text/javascript">
			window['nitroAds'].createAd('float-left-300', {
			  "refreshLimit": 0,
			  "refreshTime": 30,
			  "renderVisibleOnly": false,
			  "refreshVisibleOnly": true,
			  "sizes": [
			    [
			      "160",
			      "600"
			    ],
			    [
			      "300",
			      "250"
			    ],
			    [
			      "300",
			      "600"
			    ],
			    [
			      "320",
			      "480"
			    ],
			    [
			      "320",
			      "50"
			    ],
			    [
			      "336",
			      "280"
			    ],
			    [
			      "320",
			      "100"
			    ]
			  ],
			  "report": {
			    "enabled": true,
			    "wording": "Report Ad",
			    "position": "bottom-left"
			  },
			  "mediaQuery": '(min-width: 1820px)',
			});
		</script>
		<script type="text/javascript">
		window['nitroAds'].createAd('float-left-160', {
		  "refreshLimit": 0,
		  "refreshTime": 30,
		  "renderVisibleOnly": false,
		  "refreshVisibleOnly": true,
		  "sizes": [
		    [
		      "160",
		      "600"
		    ]
		  ],
		  "report": {
		    "enabled": true,
		    "wording": "Report Ad",
		    "position": "bottom-left"
		  },
		  "mediaQuery": '(min-width: 1550px) and (max-width: 1819px)',
		});
	</script>
	
		<div id="float-right-300"></div>
	<div id="float-right-160"></div>
			<script type="text/javascript">
			window['nitroAds'].createAd('float-right-300', {
			  "refreshLimit": 0,
			  "refreshTime": 30,
			  "renderVisibleOnly": false,
			  "refreshVisibleOnly": true,
			  "sizes": [
			    [
			      "160",
			      "600"
			    ],
			    [
			      "300",
			      "250"
			    ],
			    [
			      "300",
			      "600"
			    ],
			    [
			      "320",
			      "480"
			    ],
			    [
			      "320",
			      "50"
			    ],
			    [
			      "336",
			      "280"
			    ],
			    [
			      "320",
			      "100"
			    ]

			  ],
			  "report": {
			    "enabled": true,
			    "wording": "Report Ad",
			    "position": "bottom-left"
			  },
			  "mediaQuery": '(min-width: 1820px)',
			});
		</script>
		<script type="text/javascript">
		window['nitroAds'].createAd('float-right-160', {
		  "refreshLimit": 0,
		  "refreshTime": 30,
		  "renderVisibleOnly": false,
		  "refreshVisibleOnly": true,
		  "sizes": [
		    [
		      "160",
		      "600"
		    ]
		  ],
		  "report": {
		    "enabled": true,
		    "wording": "Report Ad",
		    "position": "bottom-left"
		  },
		  "mediaQuery": '(min-width: 1550px) and (max-width: 1819px)',
		});
	</script>
	
	

<div id="wrapper">
	
	
			<div class="col-container">
												<div class="col mod-1">

							
						<div style="margin-top: 5px;">
</div>
	
			
	

					<div style="margin-bottom: 15px;">
									<div class="js-home-stickied">
					<span class="wf-label mod-sidebar">
						Stickied Threads
					</span>
				
				<div class="wf-card mod-dark mod-sidebar">
										<a href="/24252/no-politics-religion" class="wf-module-item mod-disc mod-first" title="no politics/religion">
						
						<div class="module-item-title  mod-unread">
							no politics/religion						</div>

						
						
						
						<div class="module-item-count">
							1 
						</div>
						
											</a>
										<a href="/454104/pickems-vcl-emea-1-group-stage" class="wf-module-item mod-disc " title="Pickems: VCL EMEA #1 Group Stage">
						
						<div class="module-item-title  mod-unread">
							Pickems: VCL EMEA #1 Group Stage						</div>

						
						
						
						<div class="module-item-count">
							8 
						</div>
						
											</a>
										<a href="/454213/pickems-vct-masters-bangkok-playoffs" class="wf-module-item mod-disc " title="Pickems: VCT Masters Bangkok Playoffs">
						
						<div class="module-item-title  mod-unread">
							Pickems: VCT Masters Bangkok Playoffs						</div>

						
						
						
						<div class="module-item-count">
							28 
						</div>
						
											</a>
									</div>
			
				</div>
				
			</div>
			

					<div style="margin-bottom: 15px;">
				
					
					<div class="js-home-threads">
					
					<a href="/threads" class="wf-label mod-sidebar">
						Recent Discussion
					</a>
				
				<div class="wf-card mod-dark mod-sidebar">
										<a href="/458263/korea-esports-domination" class="wf-module-item mod-disc mod-first" title="Korea esports domination">
						
						<div class="module-item-title  mod-unread">
							Korea esports domination						</div>

						
						
						
						<div class="module-item-count">
							1 
						</div>
						
											</a>
										<a href="/458170/what-is-wrong-with-vlr" class="wf-module-item mod-disc " title="What is wrong with vlr?">
						
						<div class="module-item-title  mod-unread">
							What is wrong with vlr?						</div>

						
						
						
						<div class="module-item-count">
							21 
						</div>
						
											</a>
										<a href="/458259/fallacy" class="wf-module-item mod-disc " title="Fallacy ">
						
						<div class="module-item-title  mod-unread">
							Fallacy 						</div>

						
						
						
						<div class="module-item-count">
							14 
						</div>
						
											</a>
										<a href="/458261/g2-robbed" class="wf-module-item mod-disc " title="G2 robbed">
						
						<div class="module-item-title  mod-unread">
							G2 robbed						</div>

						
						
						
						<div class="module-item-count">
							4 
						</div>
						
											</a>
										<a href="/458260/sova-out-of-the-meta" class="wf-module-item mod-disc " title="Sova out of the meta?">
						
						<div class="module-item-title  mod-unread">
							Sova out of the meta?						</div>

						
						
						
						<div class="module-item-count">
							3 
						</div>
						
											</a>
										<a href="/458257/new-agents-too-easy" class="wf-module-item mod-disc " title="New agents too easy">
						
						<div class="module-item-title  mod-unread">
							New agents too easy						</div>

						
						
						
						<div class="module-item-count">
							7 
						</div>
						
											</a>
										<a href="/458239/waylay-meta" class="wf-module-item mod-disc " title="Waylay Meta">
						
						<div class="module-item-title  mod-unread">
							Waylay Meta						</div>

						
						
						
						<div class="module-item-count">
							12 
						</div>
						
											</a>
										<a href="/458147/totally-not-too-early-toronto-preds" class="wf-module-item mod-disc " title="totally not too early toronto preds">
						
						<div class="module-item-title  mod-unread">
							totally not too early toronto preds						</div>

						
						
						
						<div class="module-item-count">
							39 
						</div>
						
											</a>
										<a href="/458262/tens-fans-come" class="wf-module-item mod-disc " title="Tens fans come">
						
						<div class="module-item-title  mod-unread">
							Tens fans come						</div>

						
						
						
						<div class="module-item-count">
							1 
						</div>
						
											</a>
										<a href="/458258/small-quality-of-life-changes" class="wf-module-item mod-disc " title="Small quality of life changes ">
						
						<div class="module-item-title  mod-unread">
							Small quality of life changes 						</div>

						
						
						
						<div class="module-item-count">
							9 
						</div>
						
											</a>
										<a href="/458245/top-5-fun-events" class="wf-module-item mod-disc " title="top 5 fun events ">
						
						<div class="module-item-title  mod-unread">
							top 5 fun events 						</div>

						
						
						
						<div class="module-item-count">
							17 
						</div>
						
											</a>
										<a href="/457832/fun-fact" class="wf-module-item mod-disc " title="FUN FACT">
						
						<div class="module-item-title  mod-unread">
							FUN FACT						</div>

						
						
						
						<div class="module-item-count">
							2 
						</div>
						
											</a>
										<a href="/458243/best-event-ever" class="wf-module-item mod-disc " title="best event ever?">
						
						<div class="module-item-title  mod-unread">
							best event ever?						</div>

						
						
						
						<div class="module-item-count">
							17 
						</div>
						
											</a>
										<a href="/458246/will-valorant-be-over-taken-by-asia" class="wf-module-item mod-disc " title="Will Valorant be over taken by asia?">
						
						<div class="module-item-title  mod-unread">
							Will Valorant be over taken by asia?						</div>

						
						
						
						<div class="module-item-count">
							23 
						</div>
						
											</a>
										<a href="/458247/vlr-analysts-come" class="wf-module-item mod-disc " title="Vlr analysts come">
						
						<div class="module-item-title  mod-unread">
							Vlr analysts come						</div>

						
						
						
						<div class="module-item-count">
							12 
						</div>
						
											</a>
									</div>
			
				</div>
				
			</div>
			

					</div>
																<div class="col mod-2">

							
						<div style="margin-top: 5px;"></div>

	



		<div class="wf-label mod-sidebar">
		Advertisement
	</div>

		<style>
			
		
			@keyframes slide-0 {

									0% {opacity:1; z-index: 1}
									33% {opacity:0; z-index: 0}
									66% {opacity:0; z-index: 0}
									100% {opacity:0; z-index: 0}
							}

			.botd-n.mod-0 {
				animation: slide-0 9000ms infinite step-end;
			}
		
			@keyframes slide-1 {

									0% {opacity:0; z-index: 0}
									33% {opacity:1; z-index: 1}
									66% {opacity:0; z-index: 0}
									100% {opacity:0; z-index: 0}
							}

			.botd-n.mod-1 {
				animation: slide-1 9000ms infinite step-end;
			}
		
			@keyframes slide-2 {

									0% {opacity:0; z-index: 0}
									33% {opacity:0; z-index: 0}
									66% {opacity:1; z-index: 1}
									100% {opacity:0; z-index: 0}
							}

			.botd-n.mod-2 {
				animation: slide-2 9000ms infinite step-end;
			}
		
	
		.botd-n {
			color: #eee;
			background: #222;
			background: linear-gradient(165deg, #222 0%, #222 45%, hsl(263, 69%, 42%)  100%) !important;
			height: 100%;
			width: 100%;
			position: absolute;
			top: 0; left: 0;
		}
		.botd-n:hover {
		
		}
			.botd-n-main {
				margin: 5px 0;
			}
		.botd-n-event {
			color: #eee;
			max-width: 160px;
			margin: 0 auto;
			padding-top: 3px;
			text-align: center;
			text-overflow: ellipsis;
			overflow: hidden;
			text-transform: uppercase;
			font-size: 10px;
			font-style: italic;

		}
		.botd-n-team {
			display: block;
			margin-bottom: 5px;
			text-align: center;
			width: 60px;
			height: 74px;
			background: rgba(255,255,255,.15);
			clip-path: polygon(20% 0, 100% 0, 100% 80%, 80% 100%, 0 100%, 0 20%);
			padding-top: 7px;
		}
			.botd-n-team img {
				width: 25px; 
				height: 25px;
				image-rendering: -webkit-optimize-contrast;
				display: inline-block;
			}
		.botd-n-team-name {
			overflow: hidden;
			text-overflow: ellipsis;
			white-space: nowrap;
			width: 55px;
			text-align: center;
			font-size: 10px;
			font-weight: 700;
			display: block;
			margin: 6px auto;
			color: #eee;
		}
		.botd-n-team-odds {
			font-size: 11px;
			font-weight: 700;
			color: hsl(17, 100%, 55%);
		}
		.botd-n-vs {
			font-style: italic;
			width: 12px;
			text-align: center;
			font-size: 12px;
			
			margin: 0 8px;

			color: #aaa;
			font-weight: 300;
		}
		.jd8ag {
			width: 190px; height: 160px; position: relative; margin-bottom: 22px;
		}
	</style>
	


			<div class="jd8ag">
		
						
			<a href="/rr/fb/32662" class="wf-card mod-dark mod-flat botd-n mod-0">
				<div style="display: flex; justify-content: center; align-items: center; height: 38px; margin-top: 10px; ">
					<img src="/img/bet/ggbet_lt.png" style="height: 16px; margin-top: 1px;">
				</div>
				
				

				<div class="botd-n-main">
					<div style="display: flex; justify-content: center; align-items: center;">
						<div class="botd-n-team">
							<img src="//owcdn.net/img/63a531e458499.png">
							<div class="botd-n-team-name">
								MDR							</div>
							<div></div>
							<div class="botd-n-team-odds">
								1.91							</div>
						</div>
						<div class="botd-n-vs">
							vs
						</div>
						<div class="botd-n-team">
							<img src="//owcdn.net/img/664884415dd0a.png">
							<div class="botd-n-team-name">
								HGE							</div>
							<div></div>
							<div class="botd-n-team-odds">
								1.83							</div>
						</div>
					</div>
				</div>

				<div class="botd-n-event">
					VCL 25 EMEA #1				</div>
				
				
			</a>
		
						
			<a href="/rr/fb/32663" class="wf-card mod-dark mod-flat botd-n mod-1">
				<div style="display: flex; justify-content: center; align-items: center; height: 38px; margin-top: 10px; ">
					<img src="/img/bet/ggbet_lt.png" style="height: 16px; margin-top: 1px;">
				</div>
				
				

				<div class="botd-n-main">
					<div style="display: flex; justify-content: center; align-items: center;">
						<div class="botd-n-team">
							<img src="//owcdn.net/img/6712e0d973b7b.png">
							<div class="botd-n-team-name">
								BCF							</div>
							<div></div>
							<div class="botd-n-team-odds">
								1.35							</div>
						</div>
						<div class="botd-n-vs">
							vs
						</div>
						<div class="botd-n-team">
							<img src="//owcdn.net/img/60defaf8d1ec0.png">
							<div class="botd-n-team-name">
								CGN							</div>
							<div></div>
							<div class="botd-n-team-odds">
								3.07							</div>
						</div>
					</div>
				</div>

				<div class="botd-n-event">
					VCL 25 EMEA #1				</div>
				
				
			</a>
		
						
			<a href="/rr/fb/32668" class="wf-card mod-dark mod-flat botd-n mod-2">
				<div style="display: flex; justify-content: center; align-items: center; height: 38px; margin-top: 10px; ">
					<img src="/img/bet/ggbet_lt.png" style="height: 16px; margin-top: 1px;">
				</div>
				
				

				<div class="botd-n-main">
					<div style="display: flex; justify-content: center; align-items: center;">
						<div class="botd-n-team">
							<img src="//owcdn.net/img/679314d372691.png">
							<div class="botd-n-team-name">
								SRB							</div>
							<div></div>
							<div class="botd-n-team-odds">
								2.38							</div>
						</div>
						<div class="botd-n-vs">
							vs
						</div>
						<div class="botd-n-team">
							<img src="//owcdn.net/img/6793c97263739.png">
							<div class="botd-n-team-name">
								M80							</div>
							<div></div>
							<div class="botd-n-team-odds">
								1.55							</div>
						</div>
					</div>
				</div>

				<div class="botd-n-event">
					VCL 25 NA ACE: Stage 1				</div>
				
				
			</a>
				</div>
	



	

			<a class="wf-label mod-sidebar"  href="/event/2281/champions-tour-2025-masters-bangkok" >completed</a>

		<div class="wf-card mod-dark mod-sidebar more-matches">

							<a href="/449011/g2-esports-vs-t1-champions-tour-2025-masters-bangkok-gf" class="wf-module-item mm mod-first  mod-color mod-bg-after-striped_purple">
					<div style="padding-bottom: 8px; color: #888; display: flex; justify-content: space-between;">
						<div class="text-of" style="max-width: 128px;">
							Grand Final						</div>
						<div class="mm-status mod-completed">
															17h													</div>
					</div>

					<div class="mm-team text-of" style="margin-bottom: 3px;">
						<i class="flag mod-us"></i>

													G2 Esports											</div>
					<div class="mm-team text-of">
						<i class="flag mod-kr"></i>

													T1												
					</div>
				</a>
							<a href="/450589/team-international-vs-team-thailand-champions-tour-2025-masters-bangkok-main-event" class="wf-module-item mm   mod-color mod-bg-after-striped_purple">
					<div style="padding-bottom: 8px; color: #888; display: flex; justify-content: space-between;">
						<div class="text-of" style="max-width: 128px;">
							Main Event						</div>
						<div class="mm-status mod-completed">
															19h													</div>
					</div>

					<div class="mm-team text-of" style="margin-bottom: 3px;">
						<i class="flag mod-un"></i>

													Team International											</div>
					<div class="mm-team text-of">
						<i class="flag mod-th"></i>

													Team Thailand												
					</div>
				</a>
							<a href="/449013/edward-gaming-vs-t1-champions-tour-2025-masters-bangkok-lbf" class="wf-module-item mm   mod-color mod-bg-after-striped_purple">
					<div style="padding-bottom: 8px; color: #888; display: flex; justify-content: space-between;">
						<div class="text-of" style="max-width: 128px;">
							Lower Final						</div>
						<div class="mm-status mod-completed">
															1d													</div>
					</div>

					<div class="mm-team text-of" style="margin-bottom: 3px;">
						<i class="flag mod-cn"></i>

													EDward Gaming											</div>
					<div class="mm-team text-of">
						<i class="flag mod-kr"></i>

													T1												
					</div>
				</a>
							<a href="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="wf-module-item mm  mod-active mod-color mod-bg-after-striped_purple">
					<div style="padding-bottom: 8px; color: #888; display: flex; justify-content: space-between;">
						<div class="text-of" style="max-width: 128px;">
							Lower Round 1						</div>
						<div class="mm-status mod-completed">
															2d													</div>
					</div>

					<div class="mm-team text-of" style="margin-bottom: 3px;">
						<i class="flag mod-kr"></i>

													T1											</div>
					<div class="mm-team text-of">
						<i class="flag mod-eu"></i>

													Team Vitality												
					</div>
				</a>
					</div>

					<div style="color: #888; padding-right: 12px; font-size: 11px;  margin-top: -11px; text-align: right; margin-bottom: 22px;">
				... <span style="font-weight: 700">14</span> more matches
			</div>
			
					</div>
																<div class="col mod-3">

							
						
<div class="wf-card  mod-color mod-bg-after-striped_purple match-header">
	<div class="match-header-super">
		<div>
			<a href="/event/2281/champions-tour-2025-masters-bangkok/playoffs" class="match-header-event">
				
											<img src="//owcdn.net/img/603bfd7bf3f54.png" style="height: 32px; width: 32px; margin-right: 6px;">
													<div>
					<div style="font-weight: 700;">
						Champions Tour 2025: Masters Bangkok					</div>
					<div class="match-header-event-series">
						Playoffs: 
						Lower Round 1					</div>

				</div>

			</a>
		
			

			
			

					</div>
		<div style="text-align: right;">
		
			<div class="match-header-date">
				<div class="moment-tz-convert" data-utc-ts="2025-02-28 07:05:00" data-moment-format="dddd, MMMM Do">
					Friday, February 28th				</div>
									<div class="moment-tz-convert" data-utc-ts="2025-02-28 07:05:00" data-moment-format="h:mm A z" style="font-size: 12px;">

							
						5:35 PM IST					</div>
				
									<div style="margin-top: 4px;">
													<div style="font-style: italic;">
								Patch 10.02							</div>
											</div>
							</div>
		</div>
	</div>
	<div class="match-header-vs">

		<a class="match-header-link wf-link-hover mod-1"  href="/team/14/t1" >
			<div class="match-header-link-name mod-1">
				<div class="wf-title-med mod-single">
											T1									</div>
				<div class="match-header-link-name-elo">
											[1879]
									</div>
			</div>
		
												<img src="//owcdn.net/img/62fe0b8f6b084.png" alt="T1 team logo">
									</a>

		<div class="match-header-vs-score">
			<div class="match-header-vs-note">

									final
							</div>

			
							<div class="match-header-vs-score">
					<div class="js-spoiler ">
						<span class="match-header-vs-score-winner">
							2						</span>
						<span class="match-header-vs-score-colon">
							:
						</span>
						<span class="match-header-vs-score-loser">
							1						</span>
					</div>
											<div class="js-spoiler wf-spoiler" style="font-size: 24px; padding-top: 2px; padding-bottom: 6px; margin-right: -4px;">
							vs.
						</div>
									</div>
			
			<div class="match-header-vs-note">
									Bo3							</div>
		</div>

		<a class="match-header-link wf-link-hover mod-2"  href="/team/2059/team-vitality" >
												<img src="//owcdn.net/img/6466d7936fd86.png" alt="Team Vitality team logo">
										
			<div class="match-header-link-name mod-2">
				<div class="wf-title-med ">
											Team Vitality									</div>
				<div class="match-header-link-name-elo">
											[1958]
									</div>
			</div>
		</a>
	</div>

	
			<div class="match-header-note">
			T1 ban Abyss; VIT ban Pearl; T1 pick Lotus; VIT pick Haven; T1 ban Fracture; VIT ban Bind; Split remains		</div>
	</div>



	<div style="margin: 16px 0;">

		<div class="wf-label">Betting</div>

		
			
			
				<a href="/rr/bet/32657" class="wf-card mod-dark match-bet-item" rel="nofollow" target="_blank">
					<div class="match-bet-item-half" style="width: auto; flex: 1; padding-right: 20px;">
						<div>
															<img src="/img/bet/ggbet_lt.png" style="height: 13px; margin-top: 1px; image-rendering: auto;">
													</div>
				
						<div class="match-bet-item-team" style="white-space: nowrap;  flex: 1; text-align: center; font-weight: 400; word-spacing: 2px;">
							<span class="match-bet-item-odds" style="margin: 0; width: auto;">$100</span> on 
							<span class="match-bet-item-team" style="font-weight: 700; word-spacing: normal;">
																	T1															</span> 
							<span style="font-style: italic;">returned</span>
							<span class="match-bet-item-odds" style="margin: 0; width: auto;">$278</span> at 2.78 pre-match odds
						</div>
					</div>
				</a>

			
		
			
			
				<a href="/rr/bet/32660" class="wf-card mod-dark match-bet-item" rel="nofollow" target="_blank">
					<div class="match-bet-item-half" style="width: auto; flex: 1; padding-right: 20px;">
						<div>
															<img src="/img/bet/thunderpick_lt.png" style="height: 15px; margin-top: 1px; image-rendering: auto;">
													</div>
				
						<div class="match-bet-item-team" style="white-space: nowrap;  flex: 1; text-align: center; font-weight: 400; word-spacing: 2px;">
							<span class="match-bet-item-odds" style="margin: 0; width: auto;">$100</span> on 
							<span class="match-bet-item-team" style="font-weight: 700; word-spacing: normal;">
																	T1															</span> 
							<span style="font-style: italic;">returned</span>
							<span class="match-bet-item-odds" style="margin: 0; width: auto;">$270</span> at 2.70 pre-match odds
						</div>
					</div>
				</a>

			
		
	</div>



<div class="match-streams-bets-container">

	<div class="match-streams">
		<!--
		<div style="display: flex; padding: 0 20px; padding-bottom: 12px; ">

			<div class="wf-label" style="padding: 0; padding-bottom: 5px;  border-bottom: 1px dotted #aaa;">
				Official Streams
			</div>
			<div>
				/
			</div>
			<div class="wf-label" style="padding-bottom: 2px;">
				Co-streams
			</div>
		</div>
		-->
		<div class="wf-label">
			Streams
		</div>
		<div class="match-streams-container">
									
				
									<div class="wf-card mod-dark noselect match-streams-btn mod-embed  ">
						<div class="match-streams-btn-embed js-stream-embed-btn" data-site-id="valorant">
							<i class="flag mod-un" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant</span>

						</div>
						<a class="match-streams-btn-external" href="https://www.twitch.tv/valorant" target="_blank">
							<i class="fa fa-external-link"></i>
						</a>
					</div>
				
									
			
				
									<div class="wf-card mod-dark noselect match-streams-btn mod-embed  ">
						<div class="match-streams-btn-embed js-stream-embed-btn" data-site-id="valorant_id">
							<i class="flag mod-id" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant ID</span>

						</div>
						<a class="match-streams-btn-external" href="https://www.twitch.tv/valorant_id" target="_blank">
							<i class="fa fa-external-link"></i>
						</a>
					</div>
				
									
			
				
									<div class="wf-card mod-dark noselect match-streams-btn mod-embed  ">
						<div class="match-streams-btn-embed js-stream-embed-btn" data-site-id="valorant_jpn">
							<i class="flag mod-jp" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant Japan</span>

						</div>
						<a class="match-streams-btn-external" href="https://www.twitch.tv/valorant_jpn" target="_blank">
							<i class="fa fa-external-link"></i>
						</a>
					</div>
				
									
			
				
									<div class="wf-card mod-dark noselect match-streams-btn mod-embed  ">
						<div class="match-streams-btn-embed js-stream-embed-btn" data-site-id="valorant_th">
							<i class="flag mod-th" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant TH</span>

						</div>
						<a class="match-streams-btn-external" href="https://www.twitch.tv/valorant_th" target="_blank">
							<i class="fa fa-external-link"></i>
						</a>
					</div>
				
									
			
				
									<div class="wf-card mod-dark noselect match-streams-btn mod-embed  ">
						<div class="match-streams-btn-embed js-stream-embed-btn" data-site-id="valorant_tw">
							<i class="flag mod-tw" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant TW</span>

						</div>
						<a class="match-streams-btn-external" href="https://www.twitch.tv/valorant_tw" target="_blank">
							<i class="fa fa-external-link"></i>
						</a>
					</div>
				
									
			
				
									<div class="wf-card mod-dark noselect match-streams-btn mod-embed  ">
						<div class="match-streams-btn-embed js-stream-embed-btn" data-site-id="valorantesports_cn">
							<i class="flag mod-cn" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant Esports CN</span>

						</div>
						<a class="match-streams-btn-external" href="https://www.twitch.tv/valorantesports_cn" target="_blank">
							<i class="fa fa-external-link"></i>
						</a>
					</div>
				
									
			
				
									<div class="wf-card mod-dark noselect match-streams-btn mod-embed  ">
						<div class="match-streams-btn-embed js-stream-embed-btn" data-site-id="valorant_br">
							<i class="flag mod-br" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant Brazil</span>

						</div>
						<a class="match-streams-btn-external" href="https://www.twitch.tv/valorant_br" target="_blank">
							<i class="fa fa-external-link"></i>
						</a>
					</div>
				
									
			
				
									<div class="wf-card mod-dark noselect match-streams-btn mod-embed  ">
						<div class="match-streams-btn-embed js-stream-embed-btn" data-site-id="valorant_la">
							<i class="flag mod-un" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant LATAM</span>

						</div>
						<a class="match-streams-btn-external" href="https://www.twitch.tv/valorant_la" target="_blank">
							<i class="fa fa-external-link"></i>
						</a>
					</div>
				
									
			
				
									<div class="wf-card mod-dark noselect match-streams-btn mod-embed  ">
						<div class="match-streams-btn-embed js-stream-embed-btn" data-site-id="valorantleague_dach">
							<i class="flag mod-de" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant League DACH</span>

						</div>
						<a class="match-streams-btn-external" href="https://www.twitch.tv/valorantleague_dach" target="_blank">
							<i class="fa fa-external-link"></i>
						</a>
					</div>
				
									
			
				
									<div class="wf-card mod-dark noselect match-streams-btn mod-embed  ">
						<div class="match-streams-btn-embed js-stream-embed-btn" data-site-id="valorant_fr">
							<i class="flag mod-fr" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant FR</span>

						</div>
						<a class="match-streams-btn-external" href="https://www.twitch.tv/valorant_fr" target="_blank">
							<i class="fa fa-external-link"></i>
						</a>
					</div>
				
									
			
				
									<div class="wf-card mod-dark noselect match-streams-btn mod-embed  ">
						<div class="match-streams-btn-embed js-stream-embed-btn" data-site-id="valorant_tur">
							<i class="flag mod-tr" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant TR</span>

						</div>
						<a class="match-streams-btn-external" href="https://www.twitch.tv/valorant_tur" target="_blank">
							<i class="fa fa-external-link"></i>
						</a>
					</div>
				
									
			
				
									<div class="wf-card mod-dark noselect match-streams-btn mod-embed mod-hidden ">
						<div class="match-streams-btn-embed js-stream-embed-btn" data-site-id="hitpointcz">
							<i class="flag mod-cz" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">hitpointcz</span>

						</div>
						<a class="match-streams-btn-external" href="https://www.twitch.tv/hitpointcz" target="_blank">
							<i class="fa fa-external-link"></i>
						</a>
					</div>
				
									<a class="wf-card mod-dark noselect match-streams-btn mod-expand" style="padding: 0 20px; justify-content: center;">
						<div style="font-size: 10px; text-transform: uppercase;">
							... More Streams (21) 
						</div>
					
						<!--
						<div>
							<i class="fa fa-compress"></i> Collapse
						</div>
						-->
					</a>
									
			
				
									<a href="https://www.youtube.com/@ValorantEsports/live" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-un" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">VCT (YT)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.youtube.com/@VALORANTEsportsIndonesia/live" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-id" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">VAL Esports ID (YT)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.youtube.com/@VALORANTjp/live" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-jp" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant Japan (YT)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.youtube.com/@VALORANTEsportsTH/live" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-th" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">VAL Esports TH (YT)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.youtube.com/@VALORANTEsportsTW/live" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-tw" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">VAL Esports TW (YT)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.youtube.com/@VALORANTEsportsSA/live" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-in" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">VAL Esports SA (YT)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.youtube.com/@VALORANTChampionsTourVietnam/live" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-vn" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">VCT Vietnam (YT)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.youtube.com/@VALORANTEsportsCN/live" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-cn" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">VCT CN (YT)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.youtube.com/@valorantesportsbr/live" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-br" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">VAL Esports BR (YT)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.youtube.com/@VALORANTEsportsLA/live" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-un" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">VAL Esports LA (YT)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.sooplive.com/valoranten" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-un" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant (SOOP)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.sooplive.com/valorantid" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-id" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant ID (SOOP)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://play.sooplive.co.kr/valorant" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-kr" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant KR (SOOP)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://sooplive.com/valorantth" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-th" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant TH (SOOP)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.sooplive.com/valoranttw" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-tw" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant TW (SOOP)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://play.onlive.vn/valorant" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-vn" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">Valorant VN (ONLive)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://live.bilibili.com/22908869" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-cn" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">VCT (Bilibili)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.douyu.com/602" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-cn" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">VCT (Douyu)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://www.huya.com/660679" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-cn" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">VCT (Huya)</span>

						</div>
					</a>
				
									
			
				
									<a href="https://val.qq.com/act/a20230418esports/live.html?gameId=1" target="_blank" class="wf-card mod-dark match-streams-btn mod-hidden ">
						<div class="match-streams-btn-embed" style="flex: 1; text-overflow: ellipsis; white-space: nowrap; overflow: hidden; padding-right: 8px;">
							<i class="flag mod-cn" style="opacity: .8; margin-right: 3px; vertical-align: -4px;"></i>
							<span style="">VCT (QQ)</span>

						</div>
					</a>
				
									
					</div>

			</div>
	<div class="match-vods">
		<div class="wf-label" style="">
			VODs
		</div>
		<div class="match-streams-container">

			
				
				
					
											<div style="flex-basis: 100%; height: 0;"></div>
									
											<a href="https://youtu.be/9NlGE0ob-yY?t=1065" target="_blank" class="wf-card mod-dark" style="height: 37px; line-height: 37px; padding: 0 20px; margin: 0 3px; margin-bottom: 6px; flex: 1;">
							Map 1		
						</a>
					
									
											<a href="https://youtu.be/dIvMUoFOHFU?t=617" target="_blank" class="wf-card mod-dark" style="height: 37px; line-height: 37px; padding: 0 20px; margin: 0 3px; margin-bottom: 6px; flex: 1;">
							Map 2		
						</a>
					
											<div style="flex-basis: 100%; height: 0;"></div>
									
											<a href="https://youtu.be/Dzguh-SzMWk?t=478" target="_blank" class="wf-card mod-dark" style="height: 37px; line-height: 37px; padding: 0 20px; margin: 0 3px; margin-bottom: 6px; flex: 1;">
							Map 3		
						</a>
					
														</div>
	</div>
</div>


<div class="match-stream-embed js-stream-embed-target" style="position: relative;" data-host-domain="www.vlr.gg">
</div>



<div class="wf-label" style="margin-top: 16px;">
	Maps/Stats
</div>

	<div class="wf-card" style="overflow: visible;">
	<div class="vm-stats" data-match-id="86056" data-game-id="202797" data-tab="overview" data-url="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1/">
		<div style="overflow: hidden;">
			<div class="vm-stats-tabnav">
				
															<a href="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1/?game=202797&tab=overview" class="vm-stats-tabnav-item mod-first mod-active js-tab-switch" data-href="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1/?game=202797&tab=overview" data-tab="overview" data-match-id="86056">
							<div>
								<i class="fa fa-bar-chart"></i>
								Overview							</div>	
						</a>
																				<a href="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1/?game=202797&tab=performance" class="vm-stats-tabnav-item   js-tab-switch" data-href="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1/?game=202797&tab=performance" data-tab="performance" data-match-id="86056">
							<div>
								<i class="fa fa-crosshairs"></i>
								Performance							</div>	
						</a>
																				<a href="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1/?game=202797&tab=economy" class="vm-stats-tabnav-item   js-tab-switch" data-href="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1/?game=202797&tab=economy" data-tab="economy" data-match-id="86056">
							<div>
								<i class="fa fa-money"></i>
								Economy							</div>	
						</a>
																				<span class="vm-stats-tabnav-item">
							<div style="position: relative">
								<i class="fa fa-list"></i>
								Logs								<span class="ge-text-light" style="font-size: 10px;">
									(Soon)
								</span>
							</div>	
						</span>
												</div>

			
			<div class="vm-stats-gamesnav-container" style=" padding-bottom: 5px;">
								<div class="vm-stats-gamesnav noselect  ">

					
											
							<div class="vm-stats-gamesnav-item js-map-switch     mod-all mod-first" data-game-id="all" data-href="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1/?map=all" data-disabled="0">
							
					
									

										<!--
										<div class="pick ge-text-light">
											
																						
										</div>
										-->
							
								
																		All Maps
																

							

									<!--
										
										<div class="team">
											-
										</div>
																		-->
						
						
						</div>
					
											
							<div class="vm-stats-gamesnav-item js-map-switch mod-active     " data-game-id="202797" data-href="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1/?map=1" data-disabled="0">
							
					
									

										<!--
										<div class="pick ge-text-light">
											
																							Pick: T1																						
										</div>
										-->
							
								
																	<div style="margin-bottom: 2px; text-align: center; line-height: 1.5;">
										<span style="vertical-align: 4px; font-weight: 400;">1</span>
								
																					Lotus																			</div>
																

							

									<!--
																		
																					
											
																				
											
												
											<div class="team" style="margin-left: 3px;">
												
												
												<div class="team-tag" style="font-weight: 500;">VIT</div>
												<img src="//owcdn.net/img/6466d79e1ed40.png" style="width: 19px; height: 19px; image-rendering: -webkit-optimize-contrast;">
											</div>
									
									
																		-->
						
						
						</div>
					
											
							<div class="vm-stats-gamesnav-item js-map-switch      " data-game-id="202798" data-href="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1/?map=2" data-disabled="0">
							
					
									

										<!--
										<div class="pick ge-text-light">
											
																							Pick: VIT																						
										</div>
										-->
							
								
																	<div style="margin-bottom: 2px; text-align: center; line-height: 1.5;">
										<span style="vertical-align: 4px; font-weight: 400;">2</span>
								
																					Haven																			</div>
																

							

									<!--
																		
																					
											
																				
											
												
											<div class="team" style="margin-left: 3px;">
												
												
												<div class="team-tag" style="font-weight: 500;">T1</div>
												<img src="//owcdn.net/img/62fe0b8f6b084.png" style="width: 19px; height: 19px; image-rendering: -webkit-optimize-contrast;">
											</div>
									
									
																		-->
						
						
						</div>
					
											
							<div class="vm-stats-gamesnav-item js-map-switch      " data-game-id="202799" data-href="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1/?map=3" data-disabled="0">
							
					
									

										<!--
										<div class="pick ge-text-light">
											
																						
										</div>
										-->
							
								
																	<div style="margin-bottom: 2px; text-align: center; line-height: 1.5;">
										<span style="vertical-align: 4px; font-weight: 400;">3</span>
								
																					Split																			</div>
																

							

									<!--
																		
																					
											
																				
											
												
											<div class="team" style="margin-left: 3px;">
												
												
												<div class="team-tag" style="font-weight: 500;">T1</div>
												<img src="//owcdn.net/img/62fe0b8f6b084.png" style="width: 19px; height: 19px; image-rendering: -webkit-optimize-contrast;">
											</div>
									
									
																		-->
						
						
						</div>
									</div>
							</div>

		</div>

		<div class="vm-stats-loading">
				<i class="fa fa-spinner fa-spin"></i>
			</div>
			
		<div class="vm-stats-container">
			
			
			
	
	<div class="vm-stats-game mod-active" data-game-id="202797">
		
					<div class="vm-stats-game-header">
				<div class="team">
					<div class="score " style="margin-right: 12px;">12 </div>
					<div >
						<div class="team-name">
							T1						</div>
						
						<span class="mod-t">8</span> /
						<span class="mod-ct">4</span>
													/ <span class="mod-ot">0</span>
						
						
					</div>
				</div>
				<div class="map">
					<div style="font-weight: 700; font-size: 20px; text-align: center; position: relative; margin-bottom: 3px;">
						
						<span style="position: relative;">
							Lotus														<span class="picked mod-1 ge-text-light">
								PICK
							</span>
												</span>

						

						
					</div>
					<div class="map-duration ge-text-light" style="text-align: center;">
						
													1:09:37												
						
					

					</div>
				</div>
			
					
				<div class="team mod-right">
					
					<div >
						<div class="team-name">
							Team Vitality						</div>
						
						<span class="mod-ct">4</span> /
						<span class="mod-t">8</span>

													/ <span class="mod-ot">2</span>
												
					</div>
					<div class="score mod-win" style="margin-left: 8px;">14</div>
				</div>
			
			</div>
		
		<div style="text-align: center; margin-top: 15px;">
	<div style="overflow-x: auto; text-align: center;" >
		<div class="vlr-rounds">
			
							
								<div class="vlr-rounds-row">
					<div class="vlr-rounds-row-col">


						<div style="height: 12px;"></div>
						<div class="team" >
															<img src="//owcdn.net/img/62fe0b8f6b084.png">
														T1						</div>

						<div class="team">
															<img src="//owcdn.net/img/6466d7936fd86.png">
														VIT						</div>
					</div>
				
					
												<div class="vlr-rounds-row-col" title="0-1">
							<div class="rnd-num">
								1							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="1-1">
							<div class="rnd-num">
								2							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="2-1">
							<div class="rnd-num">
								3							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="3-1">
							<div class="rnd-num">
								4							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/boom.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="4-1">
							<div class="rnd-num">
								5							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/boom.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="5-1">
							<div class="rnd-num">
								6							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="6-1">
							<div class="rnd-num">
								7							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="7-1">
							<div class="rnd-num">
								8							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/boom.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="7-2">
							<div class="rnd-num">
								9							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="7-3">
							<div class="rnd-num">
								10							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="7-4">
							<div class="rnd-num">
								11							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="8-4">
							<div class="rnd-num">
								12							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
				
				
							
				
					
													<div class="vlr-rounds-row-col mod-spacing" style="width: 20px;">
							</div>

												<div class="vlr-rounds-row-col" title="9-4">
							<div class="rnd-num">
								13							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="10-4">
							<div class="rnd-num">
								14							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="10-5">
							<div class="rnd-num">
								15							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="10-6">
							<div class="rnd-num">
								16							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/boom.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="10-7">
							<div class="rnd-num">
								17							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="10-8">
							<div class="rnd-num">
								18							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="10-9">
							<div class="rnd-num">
								19							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="10-10">
							<div class="rnd-num">
								20							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="11-10">
							<div class="rnd-num">
								21							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="11-11">
							<div class="rnd-num">
								22							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/boom.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="12-11">
							<div class="rnd-num">
								23							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="12-12">
							<div class="rnd-num">
								24							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
														
						</div>
					
				
									
				</div>
				
							
								<div class="vlr-rounds-row">
					<div class="vlr-rounds-row-col">


						<div style="height: 12px;"></div>
						<div class="team" >
															<img src="//owcdn.net/img/62fe0b8f6b084.png">
														T1						</div>

						<div class="team">
															<img src="//owcdn.net/img/6466d7936fd86.png">
														VIT						</div>
					</div>
				
					
												<div class="vlr-rounds-row-col" title="12-13">
							<div class="rnd-num">
								25							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="12-14">
							<div class="rnd-num">
								26							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
														
						</div>
					
									<div style="flex: 1;">
					</div>
				
									
				</div>
				
					
		</div>
	</div>
</div>
<div style="text-align: right; margin-top: 5px; ">
	<div class="wf-filter-inset js-side-filter noselect" style="margin-bottom: 0px;">
		<div class="mod-active" data-side="both">All</div><div data-side="t">Attack</div><div data-side="ct">Defend</div>
	</div>
</div>

<div>	
	
		<div style="overflow-x: auto; margin-top: 15px; padding-bottom: 5px;">
			<table class="wf-table-inset mod-overview">
				<thead>
					<tr>
						<th></th>
						<th title="Agent"></th>
						<th title="Rating 2.0"><span>R<sup>2.0</sup><i></i></span></th>
						<th title="Average Combat Score"><span>ACS<i></i></span></th>
						<th title="Kills" style="padding-left: 14px;"><span>K<i></i></span></th>
						<th title="Deaths"><span>D<i></i></span></th>
						<th title="Assists"><span>A<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>
						<th title="Kill, Assist, Trade, Survive %""><span>KAST<i></i></span></th>
						<th title="Average Damage per Round"><span>ADR<i></i></span></th>
						<th title="Headshot %" style="padding-left: 1px;"><span>HS%<i></i></span></th>
						<th title="First Kills" style="padding-left: 9px;"><span>FK<i></i></span></th>
						<th title="First Deaths"><span>FD<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>

	
					</tr>
				</thead>
				<tbody>
						
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/13039/meteor">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Meteor 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/iso.png" alt="iso" title="Iso"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.07</span>
																					<span class="side mod-side mod-t">1.14</span>
																					<span class="side mod-side mod-ct">1.01</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">235</span>
																					<span class="side mod-side mod-t">255</span>
																					<span class="side mod-side mod-ct">215</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">21</span>
																					<span class="side mod-side mod-t">11</span>
																					<span class="side mod-side mod-ct">10</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">20</span>
																							<span class="side mod-t">9</span>
																							<span class="side mod-ct">11</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">5</span>
																					<span class="side mod-t">4</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+1</span>
																					<span class="side mod-t mod-positive">+2</span>
																					<span class="side mod-ct mod-negative">-1</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">77%</span>
																					<span class="side mod-t">92%</span>
																					<span class="side mod-ct">62%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">147</span>
																																<span class="side mod-t">153</span>
																																<span class="side mod-ct">141</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">38%</span>
																																<span class="side mod-t">43%</span>
																																<span class="side mod-ct">33%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">4</span>
																					<span class="side mod-t">3</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">3</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+1</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-positive">+1</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/485/stax">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													stax 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/sova.png" alt="sova" title="Sova"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.05</span>
																					<span class="side mod-side mod-t">1.39</span>
																					<span class="side mod-side mod-ct">0.71</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">155</span>
																					<span class="side mod-side mod-t">205</span>
																					<span class="side mod-side mod-ct">105</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">14</span>
																					<span class="side mod-side mod-t">11</span>
																					<span class="side mod-side mod-ct">3</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">15</span>
																							<span class="side mod-t">6</span>
																							<span class="side mod-ct">9</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">11</span>
																					<span class="side mod-t">3</span>
																					<span class="side mod-ct">8</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-1</span>
																					<span class="side mod-t mod-positive">+5</span>
																					<span class="side mod-ct mod-negative">-6</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">77%</span>
																					<span class="side mod-t">85%</span>
																					<span class="side mod-ct">69%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">119</span>
																																<span class="side mod-t">155</span>
																																<span class="side mod-ct">83</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">36%</span>
																																<span class="side mod-t">38%</span>
																																<span class="side mod-ct">33%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">0</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-2</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-negative">-2</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/804/buzz">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													BuZz 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/raze.png" alt="raze" title="Raze"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.97</span>
																					<span class="side mod-side mod-t">1.07</span>
																					<span class="side mod-side mod-ct">0.87</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">242</span>
																					<span class="side mod-side mod-t">276</span>
																					<span class="side mod-side mod-ct">208</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">21</span>
																					<span class="side mod-side mod-t">13</span>
																					<span class="side mod-side mod-ct">8</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">21</span>
																							<span class="side mod-t">10</span>
																							<span class="side mod-ct">11</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">5</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both ">0</span>
																					<span class="side mod-t mod-positive">+3</span>
																					<span class="side mod-ct mod-negative">-3</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">62%</span>
																					<span class="side mod-t">69%</span>
																					<span class="side mod-ct">54%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">171</span>
																																<span class="side mod-t">201</span>
																																<span class="side mod-ct">141</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">12%</span>
																																<span class="side mod-t">18%</span>
																																<span class="side mod-ct">8%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">4</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+2</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-positive">+2</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/4056/sylvan">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Sylvan 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/omen.png" alt="omen" title="Omen"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.79</span>
																					<span class="side mod-side mod-t">0.74</span>
																					<span class="side mod-side mod-ct">0.84</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">168</span>
																					<span class="side mod-side mod-t">183</span>
																					<span class="side mod-side mod-ct">153</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">14</span>
																					<span class="side mod-side mod-t">7</span>
																					<span class="side mod-side mod-ct">7</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">20</span>
																							<span class="side mod-t">10</span>
																							<span class="side mod-ct">10</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">14</span>
																					<span class="side mod-t">8</span>
																					<span class="side mod-ct">6</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-6</span>
																					<span class="side mod-t mod-negative">-3</span>
																					<span class="side mod-ct mod-negative">-3</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">81%</span>
																					<span class="side mod-t">85%</span>
																					<span class="side mod-ct">77%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">109</span>
																																<span class="side mod-t">120</span>
																																<span class="side mod-ct">98</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">28%</span>
																																<span class="side mod-t">32%</span>
																																<span class="side mod-ct">24%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+1</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-positive">+1</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/29833/izu">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													iZu 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/cypher.png" alt="cypher" title="Cypher"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.70</span>
																					<span class="side mod-side mod-t">0.59</span>
																					<span class="side mod-side mod-ct">0.82</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">145</span>
																					<span class="side mod-side mod-t">159</span>
																					<span class="side mod-side mod-ct">133</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">15</span>
																					<span class="side mod-side mod-t">7</span>
																					<span class="side mod-side mod-ct">8</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">19</span>
																							<span class="side mod-t">10</span>
																							<span class="side mod-ct">9</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">4</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-4</span>
																					<span class="side mod-t mod-negative">-3</span>
																					<span class="side mod-ct mod-negative">-1</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">58%</span>
																					<span class="side mod-t">62%</span>
																					<span class="side mod-ct">54%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">84</span>
																																<span class="side mod-t">95</span>
																																<span class="side mod-ct">73</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">27%</span>
																																<span class="side mod-t">29%</span>
																																<span class="side mod-ct">25%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">6</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">4</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-4</span>
																					<span class="side mod-t mod-negative">-1</span>
																					<span class="side mod-ct mod-negative">-3</span>
																			</span>
								</td>
							</tr>
											
				</tbody>
			</table>
		</div>
	
		<div style="overflow-x: auto; margin-top: 15px; padding-bottom: 5px;">
			<table class="wf-table-inset mod-overview">
				<thead>
					<tr>
						<th></th>
						<th title="Agent"></th>
						<th title="Rating 2.0"><span>R<sup>2.0</sup><i></i></span></th>
						<th title="Average Combat Score"><span>ACS<i></i></span></th>
						<th title="Kills" style="padding-left: 14px;"><span>K<i></i></span></th>
						<th title="Deaths"><span>D<i></i></span></th>
						<th title="Assists"><span>A<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>
						<th title="Kill, Assist, Trade, Survive %""><span>KAST<i></i></span></th>
						<th title="Average Damage per Round"><span>ADR<i></i></span></th>
						<th title="Headshot %" style="padding-left: 1px;"><span>HS%<i></i></span></th>
						<th title="First Kills" style="padding-left: 9px;"><span>FK<i></i></span></th>
						<th title="First Deaths"><span>FD<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>

	
					</tr>
				</thead>
				<tbody>
						
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-br" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Brazil"></i>

																					<a href="/player/8447/less">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Less 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/viper.png" alt="viper" title="Viper"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.46</span>
																					<span class="side mod-side mod-t">1.06</span>
																					<span class="side mod-side mod-ct">1.87</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">267</span>
																					<span class="side mod-side mod-t">195</span>
																					<span class="side mod-side mod-ct">340</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">23</span>
																					<span class="side mod-side mod-t">7</span>
																					<span class="side mod-side mod-ct">16</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">16</span>
																							<span class="side mod-t">9</span>
																							<span class="side mod-ct">7</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">12</span>
																					<span class="side mod-t">10</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+7</span>
																					<span class="side mod-t mod-negative">-2</span>
																					<span class="side mod-ct mod-positive">+9</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">85%</span>
																					<span class="side mod-t">85%</span>
																					<span class="side mod-ct">85%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">166</span>
																																<span class="side mod-t">134</span>
																																<span class="side mod-ct">198</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">36%</span>
																																<span class="side mod-t">29%</span>
																																<span class="side mod-ct">41%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both ">0</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-fi" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Finland"></i>

																					<a href="/player/5022/derke">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Derke 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/raze.png" alt="raze" title="Raze"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.26</span>
																					<span class="side mod-side mod-t">1.31</span>
																					<span class="side mod-side mod-ct">1.21</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">261</span>
																					<span class="side mod-side mod-t">318</span>
																					<span class="side mod-side mod-ct">205</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">24</span>
																					<span class="side mod-side mod-t">14</span>
																					<span class="side mod-side mod-ct">10</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">17</span>
																							<span class="side mod-t">8</span>
																							<span class="side mod-ct">9</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">5</span>
																					<span class="side mod-t">4</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+7</span>
																					<span class="side mod-t mod-positive">+6</span>
																					<span class="side mod-ct mod-positive">+1</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">69%</span>
																					<span class="side mod-t">69%</span>
																					<span class="side mod-ct">69%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">159</span>
																																<span class="side mod-t">192</span>
																																<span class="side mod-ct">127</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">25%</span>
																																<span class="side mod-t">26%</span>
																																<span class="side mod-ct">23%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">5</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">5</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both ">0</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-ru" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Russia"></i>

																					<a href="/player/2168/trexx">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													trexx 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/fade.png" alt="fade" title="Fade"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.23</span>
																					<span class="side mod-side mod-t">1.50</span>
																					<span class="side mod-side mod-ct">0.96</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">220</span>
																					<span class="side mod-side mod-t">245</span>
																					<span class="side mod-side mod-ct">196</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">20</span>
																					<span class="side mod-side mod-t">12</span>
																					<span class="side mod-side mod-ct">8</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">17</span>
																							<span class="side mod-t">6</span>
																							<span class="side mod-ct">11</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">15</span>
																					<span class="side mod-t">7</span>
																					<span class="side mod-ct">8</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+3</span>
																					<span class="side mod-t mod-positive">+6</span>
																					<span class="side mod-ct mod-negative">-3</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">77%</span>
																					<span class="side mod-t">92%</span>
																					<span class="side mod-ct">62%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">136</span>
																																<span class="side mod-t">148</span>
																																<span class="side mod-ct">125</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">12%</span>
																																<span class="side mod-t">9%</span>
																																<span class="side mod-ct">16%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+2</span>
																					<span class="side mod-t mod-positive">+2</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-ee" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Estonia"></i>

																					<a href="/player/11134/kicks">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Kicks 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/omen.png" alt="omen" title="Omen"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.93</span>
																					<span class="side mod-side mod-t">0.92</span>
																					<span class="side mod-side mod-ct">0.95</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">175</span>
																					<span class="side mod-side mod-t">155</span>
																					<span class="side mod-side mod-ct">197</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">15</span>
																					<span class="side mod-side mod-t">7</span>
																					<span class="side mod-side mod-ct">8</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">17</span>
																							<span class="side mod-t">7</span>
																							<span class="side mod-ct">10</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">12</span>
																					<span class="side mod-t">4</span>
																					<span class="side mod-ct">8</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-2</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-negative">-2</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">81%</span>
																					<span class="side mod-t">85%</span>
																					<span class="side mod-ct">77%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">111</span>
																																<span class="side mod-t">102</span>
																																<span class="side mod-ct">120</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">31%</span>
																																<span class="side mod-t">26%</span>
																																<span class="side mod-ct">35%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-1</span>
																					<span class="side mod-t mod-negative">-1</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-se" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Sweden"></i>

																					<a href="/player/312/sayf">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Sayf 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/vyse.png" alt="vyse" title="Vyse"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.73</span>
																					<span class="side mod-side mod-t">1.21</span>
																					<span class="side mod-side mod-ct">0.25</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">158</span>
																					<span class="side mod-side mod-t">191</span>
																					<span class="side mod-side mod-ct">127</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">13</span>
																					<span class="side mod-side mod-t">10</span>
																					<span class="side mod-side mod-ct">3</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">18</span>
																							<span class="side mod-t">6</span>
																							<span class="side mod-ct">12</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">8</span>
																					<span class="side mod-t">3</span>
																					<span class="side mod-ct">5</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-5</span>
																					<span class="side mod-t mod-positive">+4</span>
																					<span class="side mod-ct mod-negative">-9</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">69%</span>
																					<span class="side mod-t">85%</span>
																					<span class="side mod-ct">54%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">105</span>
																																<span class="side mod-t">116</span>
																																<span class="side mod-ct">93</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">18%</span>
																																<span class="side mod-t">39%</span>
																																<span class="side mod-ct">4%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+1</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-positive">+1</span>
																			</span>
								</td>
							</tr>
											
				</tbody>
			</table>
		</div>
	</div>		

		
	</div>

	
	<div class="vm-stats-game " data-game-id="all">
		
		
		<div style="text-align: right; margin-top: 5px; ">
	<div class="wf-filter-inset js-side-filter noselect" style="margin-bottom: 0px;">
		<div class="mod-active" data-side="both">All</div><div data-side="t">Attack</div><div data-side="ct">Defend</div>
	</div>
</div>

<div>	
	
		<div style="overflow-x: auto; margin-top: 15px; padding-bottom: 5px;">
			<table class="wf-table-inset mod-overview">
				<thead>
					<tr>
						<th></th>
						<th title="Agent"></th>
						<th title="Rating 2.0"><span>R<sup>2.0</sup><i></i></span></th>
						<th title="Average Combat Score"><span>ACS<i></i></span></th>
						<th title="Kills" style="padding-left: 14px;"><span>K<i></i></span></th>
						<th title="Deaths"><span>D<i></i></span></th>
						<th title="Assists"><span>A<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>
						<th title="Kill, Assist, Trade, Survive %""><span>KAST<i></i></span></th>
						<th title="Average Damage per Round"><span>ADR<i></i></span></th>
						<th title="Headshot %" style="padding-left: 1px;"><span>HS%<i></i></span></th>
						<th title="First Kills" style="padding-left: 9px;"><span>FK<i></i></span></th>
						<th title="First Deaths"><span>FD<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>

	
					</tr>
				</thead>
				<tbody>
						
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/804/buzz">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													BuZz 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/raze.png" alt="raze" title="Raze"></span>
									
																													
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/yoru.png" alt="yoru" title="Yoru"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-t">1.44</span>
																					<span class="side mod-side mod-ct">1.04</span>
																					<span class="side mod-side mod-both">1.20</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">270</span>
																					<span class="side mod-side mod-t">318</span>
																					<span class="side mod-side mod-ct">234</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">57</span>
																					<span class="side mod-side mod-t">28</span>
																					<span class="side mod-side mod-ct">29</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">42</span>
																							<span class="side mod-t">15</span>
																							<span class="side mod-ct">27</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">14</span>
																					<span class="side mod-t">5</span>
																					<span class="side mod-ct">9</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+15</span>
																					<span class="side mod-t mod-positive">+13</span>
																					<span class="side mod-ct mod-positive">+2</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">70%</span>
																					<span class="side mod-t">79%</span>
																					<span class="side mod-ct">65%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">168</span>
																																<span class="side mod-t">200</span>
																																<span class="side mod-ct">146</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">13%</span>
																																<span class="side mod-t">18%</span>
																																<span class="side mod-ct">10%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">15</span>
																					<span class="side mod-t">6</span>
																					<span class="side mod-ct">9</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">6</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">4</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+9</span>
																					<span class="side mod-t mod-positive">+4</span>
																					<span class="side mod-ct mod-positive">+5</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/29833/izu">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													iZu 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/cypher.png" alt="cypher" title="Cypher"></span>
									
																													
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/yoru.png" alt="yoru" title="Yoru"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-t">0.98</span>
																					<span class="side mod-side mod-ct">1.28</span>
																					<span class="side mod-side mod-both">1.16</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">213</span>
																					<span class="side mod-side mod-t">184</span>
																					<span class="side mod-side mod-ct">217</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">49</span>
																					<span class="side mod-side mod-t">15</span>
																					<span class="side mod-side mod-ct">34</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">34</span>
																							<span class="side mod-t">14</span>
																							<span class="side mod-ct">20</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">14</span>
																					<span class="side mod-t">7</span>
																					<span class="side mod-ct">7</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+15</span>
																					<span class="side mod-t mod-positive">+1</span>
																					<span class="side mod-ct mod-positive">+14</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">69%</span>
																					<span class="side mod-t">71%</span>
																					<span class="side mod-ct">68%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">119</span>
																																<span class="side mod-t">108</span>
																																<span class="side mod-ct">126</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">29%</span>
																																<span class="side mod-t">29%</span>
																																<span class="side mod-ct">30%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">6</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">5</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">10</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">8</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-4</span>
																					<span class="side mod-t mod-negative">-1</span>
																					<span class="side mod-ct mod-negative">-3</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/13039/meteor">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Meteor 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/iso.png" alt="iso" title="Iso"></span>
									
																													
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/viper.png" alt="viper" title="Viper"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-t">1.16</span>
																					<span class="side mod-side mod-ct">1.13</span>
																					<span class="side mod-side mod-both">1.14</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">233</span>
																					<span class="side mod-side mod-t">243</span>
																					<span class="side mod-side mod-ct">229</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">51</span>
																					<span class="side mod-side mod-t">20</span>
																					<span class="side mod-side mod-ct">31</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">43</span>
																							<span class="side mod-t">15</span>
																							<span class="side mod-ct">28</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">15</span>
																					<span class="side mod-t">6</span>
																					<span class="side mod-ct">9</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+8</span>
																					<span class="side mod-t mod-positive">+5</span>
																					<span class="side mod-ct mod-positive">+3</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">79%</span>
																					<span class="side mod-t">88%</span>
																					<span class="side mod-ct">73%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">146</span>
																																<span class="side mod-t">146</span>
																																<span class="side mod-ct">146</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">35%</span>
																																<span class="side mod-t">38%</span>
																																<span class="side mod-ct">33%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">10</span>
																					<span class="side mod-t">8</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">4</span>
																					<span class="side mod-t">3</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+6</span>
																					<span class="side mod-t mod-positive">+5</span>
																					<span class="side mod-ct mod-positive">+1</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/4056/sylvan">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Sylvan 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/omen.png" alt="omen" title="Omen"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-t">1.42</span>
																					<span class="side mod-side mod-ct">0.86</span>
																					<span class="side mod-side mod-both">1.08</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">176</span>
																					<span class="side mod-side mod-t">233</span>
																					<span class="side mod-side mod-ct">139</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">38</span>
																					<span class="side mod-side mod-t">21</span>
																					<span class="side mod-side mod-ct">17</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">34</span>
																							<span class="side mod-t">12</span>
																							<span class="side mod-ct">22</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">37</span>
																					<span class="side mod-t">15</span>
																					<span class="side mod-ct">22</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+4</span>
																					<span class="side mod-t mod-positive">+9</span>
																					<span class="side mod-ct mod-negative">-5</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">84%</span>
																					<span class="side mod-t">92%</span>
																					<span class="side mod-ct">78%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">113</span>
																																<span class="side mod-t">145</span>
																																<span class="side mod-ct">91</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">29%</span>
																																<span class="side mod-t">38%</span>
																																<span class="side mod-ct">22%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+1</span>
																					<span class="side mod-t mod-positive">+1</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/485/stax">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													stax 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/sova.png" alt="sova" title="Sova"></span>
									
																													
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/fade.png" alt="fade" title="Fade"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-t">1.00</span>
																					<span class="side mod-side mod-ct">1.09</span>
																					<span class="side mod-side mod-both">1.05</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">158</span>
																					<span class="side mod-side mod-t">129</span>
																					<span class="side mod-side mod-ct">176</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">35</span>
																					<span class="side mod-side mod-t">12</span>
																					<span class="side mod-side mod-ct">23</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">30</span>
																							<span class="side mod-t">10</span>
																							<span class="side mod-ct">20</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">17</span>
																					<span class="side mod-t">5</span>
																					<span class="side mod-ct">12</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+5</span>
																					<span class="side mod-t mod-positive">+2</span>
																					<span class="side mod-ct mod-positive">+3</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">80%</span>
																					<span class="side mod-t">79%</span>
																					<span class="side mod-ct">81%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">116</span>
																																<span class="side mod-t">97</span>
																																<span class="side mod-ct">128</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">34%</span>
																																<span class="side mod-t">31%</span>
																																<span class="side mod-ct">35%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-1</span>
																					<span class="side mod-t mod-negative">-1</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
											
				</tbody>
			</table>
		</div>
	
		<div style="overflow-x: auto; margin-top: 15px; padding-bottom: 5px;">
			<table class="wf-table-inset mod-overview">
				<thead>
					<tr>
						<th></th>
						<th title="Agent"></th>
						<th title="Rating 2.0"><span>R<sup>2.0</sup><i></i></span></th>
						<th title="Average Combat Score"><span>ACS<i></i></span></th>
						<th title="Kills" style="padding-left: 14px;"><span>K<i></i></span></th>
						<th title="Deaths"><span>D<i></i></span></th>
						<th title="Assists"><span>A<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>
						<th title="Kill, Assist, Trade, Survive %""><span>KAST<i></i></span></th>
						<th title="Average Damage per Round"><span>ADR<i></i></span></th>
						<th title="Headshot %" style="padding-left: 1px;"><span>HS%<i></i></span></th>
						<th title="First Kills" style="padding-left: 9px;"><span>FK<i></i></span></th>
						<th title="First Deaths"><span>FD<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>

	
					</tr>
				</thead>
				<tbody>
						
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-ru" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Russia"></i>

																					<a href="/player/2168/trexx">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													trexx 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/fade.png" alt="fade" title="Fade"></span>
									
																													
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/sova.png" alt="sova" title="Sova"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-t">1.26</span>
																					<span class="side mod-side mod-ct">0.84</span>
																					<span class="side mod-side mod-both">1.09</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">207</span>
																					<span class="side mod-side mod-t">227</span>
																					<span class="side mod-side mod-ct">182</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">41</span>
																					<span class="side mod-side mod-t">28</span>
																					<span class="side mod-side mod-ct">13</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">44</span>
																							<span class="side mod-t">23</span>
																							<span class="side mod-ct">21</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">24</span>
																					<span class="side mod-t">14</span>
																					<span class="side mod-ct">10</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-3</span>
																					<span class="side mod-t mod-positive">+5</span>
																					<span class="side mod-ct mod-negative">-8</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">66%</span>
																					<span class="side mod-t">73%</span>
																					<span class="side mod-ct">54%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">132</span>
																																<span class="side mod-t">143</span>
																																<span class="side mod-ct">114</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">18%</span>
																																<span class="side mod-t">18%</span>
																																<span class="side mod-ct">18%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+2</span>
																					<span class="side mod-t mod-positive">+2</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-fi" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Finland"></i>

																					<a href="/player/5022/derke">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Derke 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/raze.png" alt="raze" title="Raze"></span>
									
																													
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/yoru.png" alt="yoru" title="Yoru"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-t">0.99</span>
																					<span class="side mod-side mod-ct">1.05</span>
																					<span class="side mod-side mod-both">1.01</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">215</span>
																					<span class="side mod-side mod-t">237</span>
																					<span class="side mod-side mod-ct">199</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">46</span>
																					<span class="side mod-side mod-t">29</span>
																					<span class="side mod-side mod-ct">17</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">47</span>
																							<span class="side mod-t">30</span>
																							<span class="side mod-ct">17</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">9</span>
																					<span class="side mod-t">8</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-1</span>
																					<span class="side mod-t mod-negative">-1</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">64%</span>
																					<span class="side mod-t">62%</span>
																					<span class="side mod-ct">67%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">143</span>
																																<span class="side mod-t">151</span>
																																<span class="side mod-ct">130</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">24%</span>
																																<span class="side mod-t">24%</span>
																																<span class="side mod-ct">23%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">8</span>
																					<span class="side mod-t">5</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">14</span>
																					<span class="side mod-t">8</span>
																					<span class="side mod-ct">6</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-6</span>
																					<span class="side mod-t mod-negative">-3</span>
																					<span class="side mod-ct mod-negative">-3</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-br" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Brazil"></i>

																					<a href="/player/8447/less">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Less 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/viper.png" alt="viper" title="Viper"></span>
									
																													
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/cypher.png" alt="cypher" title="Cypher"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-t">0.86</span>
																					<span class="side mod-side mod-ct">1.07</span>
																					<span class="side mod-side mod-both">0.94</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">167</span>
																					<span class="side mod-side mod-t">172</span>
																					<span class="side mod-side mod-ct">199</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">37</span>
																					<span class="side mod-side mod-t">20</span>
																					<span class="side mod-side mod-ct">17</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">45</span>
																							<span class="side mod-t">28</span>
																							<span class="side mod-ct">17</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">17</span>
																					<span class="side mod-t">14</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-8</span>
																					<span class="side mod-t mod-negative">-8</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">61%</span>
																					<span class="side mod-t">62%</span>
																					<span class="side mod-ct">58%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">115</span>
																																<span class="side mod-t">113</span>
																																<span class="side mod-ct">117</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">33%</span>
																																<span class="side mod-t">29%</span>
																																<span class="side mod-ct">41%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">4</span>
																					<span class="side mod-t">4</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">6</span>
																					<span class="side mod-t">5</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-2</span>
																					<span class="side mod-t mod-negative">-1</span>
																					<span class="side mod-ct mod-negative">-1</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-se" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Sweden"></i>

																					<a href="/player/312/sayf">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Sayf 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent mod-small"><img src="/img/vlr/game/agents/vyse.png" alt="vyse" title="Vyse"></span>
									
																													
																			

											<span class="stats-sq mod-agent mod-small"><img src="/img/vlr/game/agents/jett.png" alt="jett" title="Jett"></span>
									
																													
																			

											<span class="stats-sq mod-agent mod-small"><img src="/img/vlr/game/agents/omen.png" alt="omen" title="Omen"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-t">1.02</span>
																					<span class="side mod-side mod-ct">0.28</span>
																					<span class="side mod-side mod-both">0.72</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">170</span>
																					<span class="side mod-side mod-t">204</span>
																					<span class="side mod-side mod-ct">113</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">33</span>
																					<span class="side mod-side mod-t">27</span>
																					<span class="side mod-side mod-ct">6</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">48</span>
																							<span class="side mod-t">26</span>
																							<span class="side mod-ct">22</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">14</span>
																					<span class="side mod-t">8</span>
																					<span class="side mod-ct">6</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-15</span>
																					<span class="side mod-t mod-positive">+1</span>
																					<span class="side mod-ct mod-negative">-16</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">64%</span>
																					<span class="side mod-t">76%</span>
																					<span class="side mod-ct">46%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">110</span>
																																<span class="side mod-t">129</span>
																																<span class="side mod-ct">80</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">20%</span>
																																<span class="side mod-t">26%</span>
																																<span class="side mod-ct">8%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">7</span>
																					<span class="side mod-t">4</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">5</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+2</span>
																					<span class="side mod-t mod-positive">+2</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-ee" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Estonia"></i>

																					<a href="/player/11134/kicks">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Kicks 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/omen.png" alt="omen" title="Omen"></span>
									
																													
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/breach.png" alt="breach" title="Breach"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-t">0.54</span>
																					<span class="side mod-side mod-ct">0.72</span>
																					<span class="side mod-side mod-both">0.61</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">123</span>
																					<span class="side mod-side mod-t">112</span>
																					<span class="side mod-side mod-ct">160</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">26</span>
																					<span class="side mod-side mod-t">13</span>
																					<span class="side mod-side mod-ct">13</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">46</span>
																							<span class="side mod-t">27</span>
																							<span class="side mod-ct">19</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">23</span>
																					<span class="side mod-t">14</span>
																					<span class="side mod-ct">9</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-20</span>
																					<span class="side mod-t mod-negative">-14</span>
																					<span class="side mod-ct mod-negative">-6</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">72%</span>
																					<span class="side mod-t">73%</span>
																					<span class="side mod-ct">71%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">85</span>
																																<span class="side mod-t">74</span>
																																<span class="side mod-ct">102</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">23%</span>
																																<span class="side mod-t">18%</span>
																																<span class="side mod-ct">31%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">10</span>
																					<span class="side mod-t">5</span>
																					<span class="side mod-ct">5</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-7</span>
																					<span class="side mod-t mod-negative">-3</span>
																					<span class="side mod-ct mod-negative">-4</span>
																			</span>
								</td>
							</tr>
											
				</tbody>
			</table>
		</div>
	</div>		

		
	</div>

	
	<div class="vm-stats-game " data-game-id="202798">
		
					<div class="vm-stats-game-header">
				<div class="team">
					<div class="score mod-win" style="margin-right: 12px;">13 </div>
					<div >
						<div class="team-name">
							T1						</div>
						
						<span class="mod-ct">8</span> /
						<span class="mod-t">5</span>
						
						
					</div>
				</div>
				<div class="map">
					<div style="font-weight: 700; font-size: 20px; text-align: center; position: relative; margin-bottom: 3px;">
						
						<span style="position: relative;">
							Haven														<span class="picked mod-2 ge-text-light">
								PICK
							</span>
												</span>

						

						
					</div>
					<div class="map-duration ge-text-light" style="text-align: center;">
						
													36:14												
						
					

					</div>
				</div>
			
					
				<div class="team mod-right">
					
					<div >
						<div class="team-name">
							Team Vitality						</div>
						
						<span class="mod-t">4</span> /
						<span class="mod-ct">0</span>

												
					</div>
					<div class="score " style="margin-left: 8px;">4</div>
				</div>
			
			</div>
		
		<div style="text-align: center; margin-top: 15px;">
	<div style="overflow-x: auto; text-align: center;" >
		<div class="vlr-rounds">
			
							
								<div class="vlr-rounds-row">
					<div class="vlr-rounds-row-col">


						<div style="height: 12px;"></div>
						<div class="team" >
															<img src="//owcdn.net/img/62fe0b8f6b084.png">
														T1						</div>

						<div class="team">
															<img src="//owcdn.net/img/6466d7936fd86.png">
														VIT						</div>
					</div>
				
					
												<div class="vlr-rounds-row-col" title="1-0">
							<div class="rnd-num">
								1							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="2-0">
							<div class="rnd-num">
								2							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="3-0">
							<div class="rnd-num">
								3							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="4-0">
							<div class="rnd-num">
								4							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="4-1">
							<div class="rnd-num">
								5							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/boom.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="5-1">
							<div class="rnd-num">
								6							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="5-2">
							<div class="rnd-num">
								7							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/boom.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="6-2">
							<div class="rnd-num">
								8							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="6-3">
							<div class="rnd-num">
								9							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="7-3">
							<div class="rnd-num">
								10							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="8-3">
							<div class="rnd-num">
								11							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="8-4">
							<div class="rnd-num">
								12							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
														
						</div>
					
				
				
							
				
					
													<div class="vlr-rounds-row-col mod-spacing" style="width: 20px;">
							</div>

												<div class="vlr-rounds-row-col" title="9-4">
							<div class="rnd-num">
								13							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="10-4">
							<div class="rnd-num">
								14							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="11-4">
							<div class="rnd-num">
								15							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/boom.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="12-4">
							<div class="rnd-num">
								16							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/boom.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="13-4">
							<div class="rnd-num">
								17							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="">
							<div class="rnd-num">
								18							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="">
							<div class="rnd-num">
								19							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="">
							<div class="rnd-num">
								20							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="">
							<div class="rnd-num">
								21							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="">
							<div class="rnd-num">
								22							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="">
							<div class="rnd-num">
								23							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="">
							<div class="rnd-num">
								24							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
				
									
				</div>
				
									
		</div>
	</div>
</div>
<div style="text-align: right; margin-top: 5px; ">
	<div class="wf-filter-inset js-side-filter noselect" style="margin-bottom: 0px;">
		<div class="mod-active" data-side="both">All</div><div data-side="t">Attack</div><div data-side="ct">Defend</div>
	</div>
</div>

<div>	
	
		<div style="overflow-x: auto; margin-top: 15px; padding-bottom: 5px;">
			<table class="wf-table-inset mod-overview">
				<thead>
					<tr>
						<th></th>
						<th title="Agent"></th>
						<th title="Rating 2.0"><span>R<sup>2.0</sup><i></i></span></th>
						<th title="Average Combat Score"><span>ACS<i></i></span></th>
						<th title="Kills" style="padding-left: 14px;"><span>K<i></i></span></th>
						<th title="Deaths"><span>D<i></i></span></th>
						<th title="Assists"><span>A<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>
						<th title="Kill, Assist, Trade, Survive %""><span>KAST<i></i></span></th>
						<th title="Average Damage per Round"><span>ADR<i></i></span></th>
						<th title="Headshot %" style="padding-left: 1px;"><span>HS%<i></i></span></th>
						<th title="First Kills" style="padding-left: 9px;"><span>FK<i></i></span></th>
						<th title="First Deaths"><span>FD<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>

	
					</tr>
				</thead>
				<tbody>
						
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/29833/izu">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													iZu 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/cypher.png" alt="cypher" title="Cypher"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.50</span>
																					<span class="side mod-side mod-t">2.08</span>
																					<span class="side mod-side mod-ct">1.26</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">244</span>
																					<span class="side mod-side mod-t">327</span>
																					<span class="side mod-side mod-ct">211</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">17</span>
																					<span class="side mod-side mod-t">6</span>
																					<span class="side mod-side mod-ct">11</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">8</span>
																							<span class="side mod-t">1</span>
																							<span class="side mod-ct">7</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">4</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+9</span>
																					<span class="side mod-t mod-positive">+5</span>
																					<span class="side mod-ct mod-positive">+4</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">71%</span>
																					<span class="side mod-t">80%</span>
																					<span class="side mod-ct">67%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">141</span>
																																<span class="side mod-t">185</span>
																																<span class="side mod-ct">123</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">39%</span>
																																<span class="side mod-t">42%</span>
																																<span class="side mod-ct">38%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-2</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-negative">-2</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/804/buzz">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													BuZz 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/yoru.png" alt="yoru" title="Yoru"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.27</span>
																					<span class="side mod-side mod-t">1.61</span>
																					<span class="side mod-side mod-ct">1.12</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">231</span>
																					<span class="side mod-side mod-t">290</span>
																					<span class="side mod-side mod-ct">207</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">14</span>
																					<span class="side mod-side mod-t">5</span>
																					<span class="side mod-side mod-ct">9</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">9</span>
																							<span class="side mod-t">2</span>
																							<span class="side mod-ct">7</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">4</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+5</span>
																					<span class="side mod-t mod-positive">+3</span>
																					<span class="side mod-ct mod-positive">+2</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">76%</span>
																					<span class="side mod-t">80%</span>
																					<span class="side mod-ct">75%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">149</span>
																																<span class="side mod-t">153</span>
																																<span class="side mod-ct">147</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">15%</span>
																																<span class="side mod-t">23%</span>
																																<span class="side mod-ct">11%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">5</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+4</span>
																					<span class="side mod-t mod-positive">+2</span>
																					<span class="side mod-ct mod-positive">+2</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/485/stax">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													stax 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/sova.png" alt="sova" title="Sova"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.22</span>
																					<span class="side mod-side mod-t">0.49</span>
																					<span class="side mod-side mod-ct">1.52</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">182</span>
																					<span class="side mod-side mod-t">32</span>
																					<span class="side mod-side mod-ct">246</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">11</span>
																					<span class="side mod-side mod-t">0</span>
																					<span class="side mod-side mod-ct">11</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">7</span>
																							<span class="side mod-t">2</span>
																							<span class="side mod-ct">5</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+4</span>
																					<span class="side mod-t mod-negative">-2</span>
																					<span class="side mod-ct mod-positive">+6</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">82%</span>
																					<span class="side mod-t">80%</span>
																					<span class="side mod-ct">83%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">138</span>
																																<span class="side mod-t">27</span>
																																<span class="side mod-ct">184</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">33%</span>
																																<span class="side mod-t">&nbsp;</span>
																																<span class="side mod-ct">33%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">0</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+2</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-positive">+2</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/13039/meteor">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Meteor 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/iso.png" alt="iso" title="Iso"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.15</span>
																					<span class="side mod-side mod-t">1.22</span>
																					<span class="side mod-side mod-ct">1.11</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">201</span>
																					<span class="side mod-side mod-t">234</span>
																					<span class="side mod-side mod-ct">188</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">14</span>
																					<span class="side mod-side mod-t">5</span>
																					<span class="side mod-side mod-ct">9</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">11</span>
																							<span class="side mod-t">3</span>
																							<span class="side mod-ct">8</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+3</span>
																					<span class="side mod-t mod-positive">+2</span>
																					<span class="side mod-ct mod-positive">+1</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">71%</span>
																					<span class="side mod-t">80%</span>
																					<span class="side mod-ct">67%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">120</span>
																																<span class="side mod-t">118</span>
																																<span class="side mod-ct">121</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">41%</span>
																																<span class="side mod-t">44%</span>
																																<span class="side mod-ct">39%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">3</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+2</span>
																					<span class="side mod-t mod-positive">+3</span>
																					<span class="side mod-ct mod-negative">-1</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/4056/sylvan">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Sylvan 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/omen.png" alt="omen" title="Omen"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.10</span>
																					<span class="side mod-side mod-t">2.22</span>
																					<span class="side mod-side mod-ct">0.63</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">147</span>
																					<span class="side mod-side mod-t">233</span>
																					<span class="side mod-side mod-ct">112</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">9</span>
																					<span class="side mod-side mod-t">5</span>
																					<span class="side mod-side mod-ct">4</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">7</span>
																							<span class="side mod-t">0</span>
																							<span class="side mod-ct">7</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">11</span>
																					<span class="side mod-t">4</span>
																					<span class="side mod-ct">7</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+2</span>
																					<span class="side mod-t mod-positive">+5</span>
																					<span class="side mod-ct mod-negative">-3</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">82%</span>
																					<span class="side mod-t">100%</span>
																					<span class="side mod-ct">75%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">101</span>
																																<span class="side mod-t">154</span>
																																<span class="side mod-ct">80</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">32%</span>
																																<span class="side mod-t">38%</span>
																																<span class="side mod-ct">29%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">0</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-1</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-negative">-1</span>
																			</span>
								</td>
							</tr>
											
				</tbody>
			</table>
		</div>
	
		<div style="overflow-x: auto; margin-top: 15px; padding-bottom: 5px;">
			<table class="wf-table-inset mod-overview">
				<thead>
					<tr>
						<th></th>
						<th title="Agent"></th>
						<th title="Rating 2.0"><span>R<sup>2.0</sup><i></i></span></th>
						<th title="Average Combat Score"><span>ACS<i></i></span></th>
						<th title="Kills" style="padding-left: 14px;"><span>K<i></i></span></th>
						<th title="Deaths"><span>D<i></i></span></th>
						<th title="Assists"><span>A<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>
						<th title="Kill, Assist, Trade, Survive %""><span>KAST<i></i></span></th>
						<th title="Average Damage per Round"><span>ADR<i></i></span></th>
						<th title="Headshot %" style="padding-left: 1px;"><span>HS%<i></i></span></th>
						<th title="First Kills" style="padding-left: 9px;"><span>FK<i></i></span></th>
						<th title="First Deaths"><span>FD<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>

	
					</tr>
				</thead>
				<tbody>
						
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-ru" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Russia"></i>

																					<a href="/player/2168/trexx">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													trexx 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/sova.png" alt="sova" title="Sova"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.15</span>
																					<span class="side mod-side mod-t">1.08</span>
																					<span class="side mod-side mod-ct">1.31</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">221</span>
																					<span class="side mod-side mod-t">204</span>
																					<span class="side mod-side mod-ct">264</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">11</span>
																					<span class="side mod-side mod-t">7</span>
																					<span class="side mod-side mod-ct">4</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">12</span>
																							<span class="side mod-t">8</span>
																							<span class="side mod-ct">4</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">4</span>
																					<span class="side mod-t">4</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-1</span>
																					<span class="side mod-t mod-negative">-1</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">65%</span>
																					<span class="side mod-t">67%</span>
																					<span class="side mod-ct">60%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">144</span>
																																<span class="side mod-t">140</span>
																																<span class="side mod-ct">155</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">37%</span>
																																<span class="side mod-t">30%</span>
																																<span class="side mod-ct">57%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">0</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">0</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both ">0</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-se" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Sweden"></i>

																					<a href="/player/312/sayf">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Sayf 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/jett.png" alt="jett" title="Jett"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.94</span>
																					<span class="side mod-side mod-t">1.36</span>
																					<span class="side mod-side mod-ct">0.02</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">227</span>
																					<span class="side mod-side mod-t">291</span>
																					<span class="side mod-side mod-ct">76</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">13</span>
																					<span class="side mod-side mod-t">12</span>
																					<span class="side mod-side mod-ct">1</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">14</span>
																							<span class="side mod-t">9</span>
																							<span class="side mod-ct">5</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">0</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-1</span>
																					<span class="side mod-t mod-positive">+3</span>
																					<span class="side mod-ct mod-negative">-4</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">59%</span>
																					<span class="side mod-t">75%</span>
																					<span class="side mod-ct">20%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">157</span>
																																<span class="side mod-t">204</span>
																																<span class="side mod-ct">46</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">20%</span>
																																<span class="side mod-t">21%</span>
																																<span class="side mod-ct">0%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+1</span>
																					<span class="side mod-t mod-positive">+2</span>
																					<span class="side mod-ct mod-negative">-1</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-fi" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Finland"></i>

																					<a href="/player/5022/derke">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Derke 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/yoru.png" alt="yoru" title="Yoru"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.88</span>
																					<span class="side mod-side mod-t">1.05</span>
																					<span class="side mod-side mod-ct">0.47</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">175</span>
																					<span class="side mod-side mod-t">212</span>
																					<span class="side mod-side mod-ct">88</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">9</span>
																					<span class="side mod-side mod-t">8</span>
																					<span class="side mod-side mod-ct">1</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">13</span>
																							<span class="side mod-t">10</span>
																							<span class="side mod-ct">3</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">3</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-4</span>
																					<span class="side mod-t mod-negative">-2</span>
																					<span class="side mod-ct mod-negative">-2</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">59%</span>
																					<span class="side mod-t">58%</span>
																					<span class="side mod-ct">60%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">124</span>
																																<span class="side mod-t">142</span>
																																<span class="side mod-ct">80</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">22%</span>
																																<span class="side mod-t">24%</span>
																																<span class="side mod-ct">13%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">3</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">5</span>
																					<span class="side mod-t">3</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-2</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-negative">-2</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-ee" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Estonia"></i>

																					<a href="/player/11134/kicks">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Kicks 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/omen.png" alt="omen" title="Omen"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.40</span>
																					<span class="side mod-side mod-t">0.51</span>
																					<span class="side mod-side mod-ct">0.14</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">102</span>
																					<span class="side mod-side mod-t">102</span>
																					<span class="side mod-side mod-ct">101</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">6</span>
																					<span class="side mod-side mod-t">4</span>
																					<span class="side mod-side mod-ct">2</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">13</span>
																							<span class="side mod-t">8</span>
																							<span class="side mod-ct">5</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">5</span>
																					<span class="side mod-t">5</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-7</span>
																					<span class="side mod-t mod-negative">-4</span>
																					<span class="side mod-ct mod-negative">-3</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">65%</span>
																					<span class="side mod-t">75%</span>
																					<span class="side mod-ct">40%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">65</span>
																																<span class="side mod-t">68</span>
																																<span class="side mod-ct">56</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">20%</span>
																																<span class="side mod-t">21%</span>
																																<span class="side mod-ct">17%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">0</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-3</span>
																					<span class="side mod-t mod-negative">-2</span>
																					<span class="side mod-ct mod-negative">-1</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-br" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Brazil"></i>

																					<a href="/player/8447/less">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Less 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/cypher.png" alt="cypher" title="Cypher"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.26</span>
																					<span class="side mod-side mod-t">0.38</span>
																					<span class="side mod-side mod-ct">0.03</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">58</span>
																					<span class="side mod-side mod-t">78</span>
																					<span class="side mod-side mod-ct">10</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">3</span>
																					<span class="side mod-side mod-t">3</span>
																					<span class="side mod-side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">13</span>
																							<span class="side mod-t">9</span>
																							<span class="side mod-ct">4</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-10</span>
																					<span class="side mod-t mod-negative">-6</span>
																					<span class="side mod-ct mod-negative">-4</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">41%</span>
																					<span class="side mod-t">50%</span>
																					<span class="side mod-ct">20%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">44</span>
																																<span class="side mod-t">58</span>
																																<span class="side mod-ct">10</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">23%</span>
																																<span class="side mod-t">27%</span>
																																<span class="side mod-ct">0%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-1</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-negative">-1</span>
																			</span>
								</td>
							</tr>
											
				</tbody>
			</table>
		</div>
	</div>		

		
	</div>

	
	<div class="vm-stats-game " data-game-id="202799">
		
					<div class="vm-stats-game-header">
				<div class="team">
					<div class="score mod-win" style="margin-right: 12px;">13 </div>
					<div >
						<div class="team-name">
							T1						</div>
						
						<span class="mod-ct">9</span> /
						<span class="mod-t">4</span>
						
						
					</div>
				</div>
				<div class="map">
					<div style="font-weight: 700; font-size: 20px; text-align: center; position: relative; margin-bottom: 3px;">
						
						<span style="position: relative;">
							Split													</span>

						

						
					</div>
					<div class="map-duration ge-text-light" style="text-align: center;">
						
													42:08												
						
					

					</div>
				</div>
			
					
				<div class="team mod-right">
					
					<div >
						<div class="team-name">
							Team Vitality						</div>
						
						<span class="mod-t">3</span> /
						<span class="mod-ct">2</span>

												
					</div>
					<div class="score " style="margin-left: 8px;">5</div>
				</div>
			
			</div>
		
		<div style="text-align: center; margin-top: 15px;">
	<div style="overflow-x: auto; text-align: center;" >
		<div class="vlr-rounds">
			
							
								<div class="vlr-rounds-row">
					<div class="vlr-rounds-row-col">


						<div style="height: 12px;"></div>
						<div class="team" >
															<img src="//owcdn.net/img/62fe0b8f6b084.png">
														T1						</div>

						<div class="team">
															<img src="//owcdn.net/img/6466d7936fd86.png">
														VIT						</div>
					</div>
				
					
												<div class="vlr-rounds-row-col" title="0-1">
							<div class="rnd-num">
								1							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="1-1">
							<div class="rnd-num">
								2							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="2-1">
							<div class="rnd-num">
								3							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="2-2">
							<div class="rnd-num">
								4							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="3-2">
							<div class="rnd-num">
								5							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="4-2">
							<div class="rnd-num">
								6							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="5-2">
							<div class="rnd-num">
								7							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="6-2">
							<div class="rnd-num">
								8							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="7-2">
							<div class="rnd-num">
								9							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/time.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="8-2">
							<div class="rnd-num">
								10							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="8-3">
							<div class="rnd-num">
								11							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="9-3">
							<div class="rnd-num">
								12							</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
				
				
							
				
					
													<div class="vlr-rounds-row-col mod-spacing" style="width: 20px;">
							</div>

												<div class="vlr-rounds-row-col" title="10-3">
							<div class="rnd-num">
								13							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="10-4">
							<div class="rnd-num">
								14							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="10-5">
							<div class="rnd-num">
								15							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq mod-win mod-ct">
																														<img src="/img/vlr/game/round/defuse.webp">
																			
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="11-5">
							<div class="rnd-num">
								16							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/boom.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="12-5">
							<div class="rnd-num">
								17							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="13-5">
							<div class="rnd-num">
								18							</div>
							
								<div class="rnd-sq mod-win mod-t">
																														<img src="/img/vlr/game/round/elim.webp">
																			
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="">
							<div class="rnd-num">
								19							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="">
							<div class="rnd-num">
								20							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="">
							<div class="rnd-num">
								21							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="">
							<div class="rnd-num">
								22							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="">
							<div class="rnd-num">
								23							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
												<div class="vlr-rounds-row-col" title="">
							<div class="rnd-num">
								24							</div>
							
								<div class="rnd-sq ">
									
								</div>
							
								<div class="rnd-sq ">
									
								</div>
														
						</div>
					
				
									
				</div>
				
									
		</div>
	</div>
</div>
<div style="text-align: right; margin-top: 5px; ">
	<div class="wf-filter-inset js-side-filter noselect" style="margin-bottom: 0px;">
		<div class="mod-active" data-side="both">All</div><div data-side="t">Attack</div><div data-side="ct">Defend</div>
	</div>
</div>

<div>	
	
		<div style="overflow-x: auto; margin-top: 15px; padding-bottom: 5px;">
			<table class="wf-table-inset mod-overview">
				<thead>
					<tr>
						<th></th>
						<th title="Agent"></th>
						<th title="Rating 2.0"><span>R<sup>2.0</sup><i></i></span></th>
						<th title="Average Combat Score"><span>ACS<i></i></span></th>
						<th title="Kills" style="padding-left: 14px;"><span>K<i></i></span></th>
						<th title="Deaths"><span>D<i></i></span></th>
						<th title="Assists"><span>A<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>
						<th title="Kill, Assist, Trade, Survive %""><span>KAST<i></i></span></th>
						<th title="Average Damage per Round"><span>ADR<i></i></span></th>
						<th title="Headshot %" style="padding-left: 1px;"><span>HS%<i></i></span></th>
						<th title="First Kills" style="padding-left: 9px;"><span>FK<i></i></span></th>
						<th title="First Deaths"><span>FD<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>

	
					</tr>
				</thead>
				<tbody>
						
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/29833/izu">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													iZu 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/yoru.png" alt="yoru" title="Yoru"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.51</span>
																					<span class="side mod-side mod-t">0.91</span>
																					<span class="side mod-side mod-ct">1.81</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">249</span>
																					<span class="side mod-side mod-t">119</span>
																					<span class="side mod-side mod-ct">314</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">17</span>
																					<span class="side mod-side mod-t">2</span>
																					<span class="side mod-side mod-ct">15</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">7</span>
																							<span class="side mod-t">3</span>
																							<span class="side mod-ct">4</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">6</span>
																					<span class="side mod-t">4</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+10</span>
																					<span class="side mod-t mod-negative">-1</span>
																					<span class="side mod-ct mod-positive">+11</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">83%</span>
																					<span class="side mod-t">83%</span>
																					<span class="side mod-ct">83%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">149</span>
																																<span class="side mod-t">70</span>
																																<span class="side mod-ct">188</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">24%</span>
																																<span class="side mod-t">11%</span>
																																<span class="side mod-ct">27%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+2</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-positive">+2</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/4056/sylvan">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Sylvan 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/omen.png" alt="omen" title="Omen"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.48</span>
																					<span class="side mod-side mod-t">2.23</span>
																					<span class="side mod-side mod-ct">1.11</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">213</span>
																					<span class="side mod-side mod-t">341</span>
																					<span class="side mod-side mod-ct">149</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">15</span>
																					<span class="side mod-side mod-t">9</span>
																					<span class="side mod-side mod-ct">6</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">7</span>
																							<span class="side mod-t">2</span>
																							<span class="side mod-ct">5</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">12</span>
																					<span class="side mod-t">3</span>
																					<span class="side mod-ct">9</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+8</span>
																					<span class="side mod-t mod-positive">+7</span>
																					<span class="side mod-ct mod-positive">+1</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">89%</span>
																					<span class="side mod-t">100%</span>
																					<span class="side mod-ct">83%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">128</span>
																																<span class="side mod-t">194</span>
																																<span class="side mod-ct">95</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">28%</span>
																																<span class="side mod-t">47%</span>
																																<span class="side mod-ct">16%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">0</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+1</span>
																					<span class="side mod-t mod-positive">+1</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/804/buzz">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													BuZz 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/raze.png" alt="raze" title="Raze"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.47</span>
																					<span class="side mod-side mod-t">2.10</span>
																					<span class="side mod-side mod-ct">1.15</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">337</span>
																					<span class="side mod-side mod-t">431</span>
																					<span class="side mod-side mod-ct">290</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">22</span>
																					<span class="side mod-side mod-t">10</span>
																					<span class="side mod-side mod-ct">12</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">12</span>
																							<span class="side mod-t">3</span>
																							<span class="side mod-ct">9</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">5</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+10</span>
																					<span class="side mod-t mod-positive">+7</span>
																					<span class="side mod-ct mod-positive">+3</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">78%</span>
																					<span class="side mod-t">100%</span>
																					<span class="side mod-ct">67%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">181</span>
																																<span class="side mod-t">238</span>
																																<span class="side mod-ct">152</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">13%</span>
																																<span class="side mod-t">15%</span>
																																<span class="side mod-ct">12%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">6</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">4</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+3</span>
																					<span class="side mod-t mod-positive">+2</span>
																					<span class="side mod-ct mod-positive">+1</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/13039/meteor">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Meteor 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/viper.png" alt="viper" title="Viper"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">1.25</span>
																					<span class="side mod-side mod-t">1.16</span>
																					<span class="side mod-side mod-ct">1.29</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">264</span>
																					<span class="side mod-side mod-t">226</span>
																					<span class="side mod-side mod-ct">284</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">16</span>
																					<span class="side mod-side mod-t">4</span>
																					<span class="side mod-side mod-ct">12</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">12</span>
																							<span class="side mod-t">3</span>
																							<span class="side mod-ct">9</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">7</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">5</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+4</span>
																					<span class="side mod-t mod-positive">+1</span>
																					<span class="side mod-ct mod-positive">+3</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">89%</span>
																					<span class="side mod-t">83%</span>
																					<span class="side mod-ct">92%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">170</span>
																																<span class="side mod-t">155</span>
																																<span class="side mod-ct">178</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">29%</span>
																																<span class="side mod-t">27%</span>
																																<span class="side mod-ct">30%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">0</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+3</span>
																					<span class="side mod-t mod-positive">+2</span>
																					<span class="side mod-ct mod-positive">+1</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-kr" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="South Korea"></i>

																					<a href="/player/485/stax">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													stax 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													T1												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/fade.png" alt="fade" title="Fade"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.91</span>
																					<span class="side mod-side mod-t">0.57</span>
																					<span class="side mod-side mod-ct">1.07</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">137</span>
																					<span class="side mod-side mod-t">43</span>
																					<span class="side mod-side mod-ct">184</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">10</span>
																					<span class="side mod-side mod-t">1</span>
																					<span class="side mod-side mod-ct">9</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">8</span>
																							<span class="side mod-t">2</span>
																							<span class="side mod-ct">6</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-positive">+2</span>
																					<span class="side mod-t mod-negative">-1</span>
																					<span class="side mod-ct mod-positive">+3</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">83%</span>
																					<span class="side mod-t">67%</span>
																					<span class="side mod-ct">92%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">91</span>
																																<span class="side mod-t">29</span>
																																<span class="side mod-ct">122</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">30%</span>
																																<span class="side mod-t">0%</span>
																																<span class="side mod-ct">39%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">0</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-1</span>
																					<span class="side mod-t mod-negative">-1</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
											
				</tbody>
			</table>
		</div>
	
		<div style="overflow-x: auto; margin-top: 15px; padding-bottom: 5px;">
			<table class="wf-table-inset mod-overview">
				<thead>
					<tr>
						<th></th>
						<th title="Agent"></th>
						<th title="Rating 2.0"><span>R<sup>2.0</sup><i></i></span></th>
						<th title="Average Combat Score"><span>ACS<i></i></span></th>
						<th title="Kills" style="padding-left: 14px;"><span>K<i></i></span></th>
						<th title="Deaths"><span>D<i></i></span></th>
						<th title="Assists"><span>A<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>
						<th title="Kill, Assist, Trade, Survive %""><span>KAST<i></i></span></th>
						<th title="Average Damage per Round"><span>ADR<i></i></span></th>
						<th title="Headshot %" style="padding-left: 1px;"><span>HS%<i></i></span></th>
						<th title="First Kills" style="padding-left: 9px;"><span>FK<i></i></span></th>
						<th title="First Deaths"><span>FD<i></i></span></th>
						<th title="Kills - Deaths"><span>+/&ndash;<i></i></span></th>

	
					</tr>
				</thead>
				<tbody>
						
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-ru" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Russia"></i>

																					<a href="/player/2168/trexx">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													trexx 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/fade.png" alt="fade" title="Fade"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.84</span>
																					<span class="side mod-side mod-t">1.17</span>
																					<span class="side mod-side mod-ct">0.19</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">181</span>
																					<span class="side mod-side mod-t">230</span>
																					<span class="side mod-side mod-ct">83</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">10</span>
																					<span class="side mod-side mod-t">9</span>
																					<span class="side mod-side mod-ct">1</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">15</span>
																							<span class="side mod-t">9</span>
																							<span class="side mod-ct">6</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">5</span>
																					<span class="side mod-t">3</span>
																					<span class="side mod-ct">2</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-5</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-negative">-5</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">50%</span>
																					<span class="side mod-t">58%</span>
																					<span class="side mod-ct">33%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">114</span>
																																<span class="side mod-t">143</span>
																																<span class="side mod-ct">55</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">16%</span>
																																<span class="side mod-t">22%</span>
																																<span class="side mod-ct">0%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">0</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">0</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both ">0</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-br" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Brazil"></i>

																					<a href="/player/8447/less">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Less 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/viper.png" alt="viper" title="Viper"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.83</span>
																					<span class="side mod-side mod-t">1.14</span>
																					<span class="side mod-side mod-ct">0.22</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">176</span>
																					<span class="side mod-side mod-t">239</span>
																					<span class="side mod-side mod-ct">51</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">11</span>
																					<span class="side mod-side mod-t">10</span>
																					<span class="side mod-side mod-ct">1</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">16</span>
																							<span class="side mod-t">10</span>
																							<span class="side mod-ct">6</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-5</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-negative">-5</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">44%</span>
																					<span class="side mod-t">50%</span>
																					<span class="side mod-ct">33%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">106</span>
																																<span class="side mod-t">144</span>
																																<span class="side mod-ct">30</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">32%</span>
																																<span class="side mod-t">30%</span>
																																<span class="side mod-ct">100%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">2</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">3</span>
																					<span class="side mod-t">3</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-1</span>
																					<span class="side mod-t mod-negative">-1</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-fi" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Finland"></i>

																					<a href="/player/5022/derke">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Derke 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/raze.png" alt="raze" title="Raze"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.77</span>
																					<span class="side mod-side mod-t">0.57</span>
																					<span class="side mod-side mod-ct">1.18</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">209</span>
																					<span class="side mod-side mod-t">175</span>
																					<span class="side mod-side mod-ct">280</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">13</span>
																					<span class="side mod-side mod-t">7</span>
																					<span class="side mod-side mod-ct">6</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">17</span>
																							<span class="side mod-t">12</span>
																							<span class="side mod-ct">5</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-4</span>
																					<span class="side mod-t mod-negative">-5</span>
																					<span class="side mod-ct mod-positive">+1</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">61%</span>
																					<span class="side mod-t">58%</span>
																					<span class="side mod-ct">67%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">136</span>
																																<span class="side mod-t">116</span>
																																<span class="side mod-ct">178</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">24%</span>
																																<span class="side mod-t">21%</span>
																																<span class="side mod-ct">28%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">0</span>
																					<span class="side mod-t">0</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">4</span>
																					<span class="side mod-t">3</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-4</span>
																					<span class="side mod-t mod-negative">-3</span>
																					<span class="side mod-ct mod-negative">-1</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-se" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Sweden"></i>

																					<a href="/player/312/sayf">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Sayf 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/omen.png" alt="omen" title="Omen"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.50</span>
																					<span class="side mod-side mod-t">0.47</span>
																					<span class="side mod-side mod-ct">0.54</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">124</span>
																					<span class="side mod-side mod-t">130</span>
																					<span class="side mod-side mod-ct">113</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">7</span>
																					<span class="side mod-side mod-t">5</span>
																					<span class="side mod-side mod-ct">2</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">16</span>
																							<span class="side mod-t">11</span>
																							<span class="side mod-ct">5</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">6</span>
																					<span class="side mod-t">5</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-9</span>
																					<span class="side mod-t mod-negative">-6</span>
																					<span class="side mod-ct mod-negative">-3</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">61%</span>
																					<span class="side mod-t">67%</span>
																					<span class="side mod-ct">50%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">72</span>
																																<span class="side mod-t">67</span>
																																<span class="side mod-ct">82</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">27%</span>
																																<span class="side mod-t">25%</span>
																																<span class="side mod-ct">33%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">2</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both ">0</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct ">0</span>
																			</span>
								</td>
							</tr>
							

														
							<tr>
								<td class="mod-player" style=" padding-right: 10px;">
									<div style="display: flex; align-items: center;" >
																		
										<i class="flag mod-ee" style="opacity: .7; margin-right: 8px; vertical-align: -1px; margin-left: 2px;" title="Estonia"></i>

																					<a href="/player/11134/kicks">	
												<div style="font-weight: 700; padding-bottom: 4px; padding-top: 2px; max-width: 80px;" class="text-of">
													Kicks 
													
												</div>
												<div class="ge-text-light" style="text-transform: uppercase; font-size: 11px;">
													
													VIT												</div>
											</a>
																			</div>
								</td>
								<td class="mod-agents">
									<div style="white-space: nowrap; height: 28px; display: flex; align-items: center; justify-content: flex-end;">
									
																			
																			

											<span class="stats-sq mod-agent small"><img src="/img/vlr/game/agents/breach.png" alt="breach" title="Breach"></span>
									
																												</div>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">0.35</span>
																					<span class="side mod-side mod-t">0.17</span>
																					<span class="side mod-side mod-ct">0.71</span>
																			</span>
								</td>
								
								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-side mod-both">93</span>
																					<span class="side mod-side mod-t">75</span>
																					<span class="side mod-side mod-ct">130</span>
																			</span>
								</td>

								<td class="mod-stat mod-vlr-kills"> 
									<span class="stats-sq">
																					<span class="side mod-side mod-both">5</span>
																					<span class="side mod-side mod-t">2</span>
																					<span class="side mod-side mod-ct">3</span>
																			</span>
								</td>
								<td class="mod-stat mod-vlr-deaths"> 
									<span class="stats-sq">
										<span class="num-space">/</span>
										<span style="margin: 0 4px;">
																							<span class="side mod-both">16</span>
																							<span class="side mod-t">12</span>
																							<span class="side mod-ct">4</span>
																					</span>
										<span class="num-space">/</span>
									</span>
								</td>
								<td class="mod-stat mod-vlr-assists"> 
									<span class="stats-sq">
																					<span class="side mod-both">6</span>
																					<span class="side mod-t">5</span>
																					<span class="side mod-ct">1</span>
																			</span>
								</td>

								<td class="mod-stat mod-kd-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-11</span>
																					<span class="side mod-t mod-negative">-10</span>
																					<span class="side mod-ct mod-negative">-1</span>
																			</span>
								</td>

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																					<span class="side mod-both">67%</span>
																					<span class="side mod-t">58%</span>
																					<span class="side mod-ct">83%</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq mod-combat" style="width: 36px;">
																																<span class="side mod-both">67</span>
																																<span class="side mod-t">49</span>
																																<span class="side mod-ct">102</span>
																			</span>
								</td>	

								<td class="mod-stat"> 
									<span class="stats-sq" style="width: 36px;">
																																<span class="side mod-both">14%</span>
																																<span class="side mod-t">5%</span>
																																<span class="side mod-ct">30%</span>
																			</span>
								</td>
							
								<td class="mod-stat mod-fb"> 
									<span class="stats-sq">
																					<span class="side mod-both">1</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">0</span>
																			</span>
								</td>
								<td class="mod-stat mod-fd"> 
									<span class="stats-sq">
																					<span class="side mod-both">4</span>
																					<span class="side mod-t">1</span>
																					<span class="side mod-ct">3</span>
																			</span>
								</td>

								<td class="mod-stat mod-fk-diff"> 
									<span class="stats-sq" style="width: 32px;">
																					<span class="side mod-both mod-negative">-3</span>
																					<span class="side mod-t ">0</span>
																					<span class="side mod-ct mod-negative">-3</span>
																			</span>
								</td>
							</tr>
											
				</tbody>
			</table>
		</div>
	</div>		

		
	</div>

		</div>
	</div>
</div>







	<div class="wf-label">
		Head-to-head
	</div>
	<div class="wf-card match-h2h ">
		<div style="font-size: 10px; color: #aaa; text-transform: uppercase;">
		</div>
		<div class="wf-module-item match-h2h-header mod-first">

			<a href="/team/14/t1" class="match-h2h-header-team">
				
											<img src="//owcdn.net/img/62fe0b8f6b084.png">
					
								<div>T1</div>
			</a>

			<!--
			<div class="match-h2h-header-count">
				0				<div class="match-h2h-header-count-label">
					Wins
				</div>
			</div>
			<div class="match-h2h-header-count mod-center">
							</div>
			<div class="match-h2h-header-count">
				1				<div class="match-h2h-header-count-label">
					Wins
				</div>
			</div>
			-->
			
			<a href="/team/2059/team-vitality" class="match-h2h-header-team mod-right">
				<div>Team Vitality</div>
					

											<img src="//owcdn.net/img/6466d7936fd86.png">
												</a>
		</div>
					<div class="match-h2h-matches">
									<a href="/448599/team-vitality-vs-t1-champions-tour-2025-masters-bangkok-r1" class="wf-module-item mod-h2h ">
						<div class="match-h2h-matches-event">
															<img src="//owcdn.net/img/603bfd7bf3f54.png" style="height: 32px; margin-right: 10px;">
														<div>
								<div class="match-h2h-matches-event-name text-of">VCT 25: Masters Bangkok</div>
								<div class="match-h2h-matches-event-series text-of">R1</div>
							</div>
						</div>
						<div style="display: flex; align-items: center;">
						
							
																	<img src="//owcdn.net/img/62fe0b8f6b084.png" class="match-h2h-matches-team ">
								
							
							<div class="match-h2h-matches-score">
								<span class="rf ">0</span>
								<span class="ra mod-win" style="margin-left: 2px;">2</span>
								
							</div>
						
							
																	<img src="//owcdn.net/img/6466d7936fd86.png" class="match-h2h-matches-team mod-win">
														
									
						</div>
						<div class="match-h2h-matches-date">
							 2025/02/21						</div>
					</a>
				
							</div>
			</div>
	<div class="wf-label">
		Past Matches
	</div>
	<div style="display: flex;">
					<div class="wf-card mod-dark match-histories mod-first mod-loss">

				
																	<a href="/449008/edward-gaming-vs-t1-champions-tour-2025-masters-bangkok-ubsf" class="match-histories-item wf-module-item mod-first mod-loss">
							
							<div class="match-histories-item-result mod-loss">
								<span class="rf">1</span>
								<span class="ra">2</span>
							</div> 
							<div class="match-histories-item-opponent" style="min-width: 0;">
								<span style="font-style: italic;">vs.</span>

																	<img src="//owcdn.net/img/62c82049253b2.png" class="match-histories-item-opponent-logo">
																<span class="match-histories-item-opponent-name text-of">EDward Gaming</span>

							</div>
							<div class="match-histories-item-date">
								2025/02/27							</div>
						</a>
									
																	<a href="/449004/t1-vs-drx-champions-tour-2025-masters-bangkok-r3" class="match-histories-item wf-module-item  mod-win">
							
							<div class="match-histories-item-result mod-win">
								<span class="rf">2</span>
								<span class="ra">0</span>
							</div> 
							<div class="match-histories-item-opponent" style="min-width: 0;">
								<span style="font-style: italic;">vs.</span>

																	<img src="//owcdn.net/img/63b17abd77fc0.png" class="match-histories-item-opponent-logo">
																<span class="match-histories-item-opponent-name text-of">DRX</span>

							</div>
							<div class="match-histories-item-date">
								2025/02/24							</div>
						</a>
									
																	<a href="/449002/t1-vs-trace-esports-champions-tour-2025-masters-bangkok-r2-0-1" class="match-histories-item wf-module-item  mod-win">
							
							<div class="match-histories-item-result mod-win">
								<span class="rf">2</span>
								<span class="ra">0</span>
							</div> 
							<div class="match-histories-item-opponent" style="min-width: 0;">
								<span style="font-style: italic;">vs.</span>

																	<img src="//owcdn.net/img/6433a2cc3ae72.png" class="match-histories-item-opponent-logo">
																<span class="match-histories-item-opponent-name text-of">Trace Esports</span>

							</div>
							<div class="match-histories-item-date">
								2025/02/23							</div>
						</a>
									
																	<a href="/448599/team-vitality-vs-t1-champions-tour-2025-masters-bangkok-r1" class="match-histories-item wf-module-item  mod-loss">
							
							<div class="match-histories-item-result mod-loss">
								<span class="rf">0</span>
								<span class="ra">2</span>
							</div> 
							<div class="match-histories-item-opponent" style="min-width: 0;">
								<span style="font-style: italic;">vs.</span>

																	<img src="//owcdn.net/img/6466d79e1ed40.png" class="match-histories-item-opponent-logo">
																<span class="match-histories-item-opponent-name text-of">Team Vitality</span>

							</div>
							<div class="match-histories-item-date">
								2025/02/21							</div>
						</a>
									
																	<a href="/430525/drx-vs-t1-champions-tour-2025-pacific-kickoff-gf" class="match-histories-item wf-module-item  mod-loss">
							
							<div class="match-histories-item-result mod-loss">
								<span class="rf">2</span>
								<span class="ra">3</span>
							</div> 
							<div class="match-histories-item-opponent" style="min-width: 0;">
								<span style="font-style: italic;">vs.</span>

																	<img src="//owcdn.net/img/63b17abd77fc0.png" class="match-histories-item-opponent-logo">
																<span class="match-histories-item-opponent-name text-of">DRX</span>

							</div>
							<div class="match-histories-item-date">
								2025/02/09							</div>
						</a>
									
			</div>
					<div class="wf-card mod-dark match-histories  mod-loss">

				
																	<a href="/449009/team-vitality-vs-g2-esports-champions-tour-2025-masters-bangkok-ubsf" class="match-histories-item wf-module-item mod-first mod-loss">
							
							<div class="match-histories-item-result mod-loss">
								<span class="rf">0</span>
								<span class="ra">2</span>
							</div> 
							<div class="match-histories-item-opponent" style="min-width: 0;">
								<span style="font-style: italic;">vs.</span>

																	<img src="//owcdn.net/img/633822848a741.png" class="match-histories-item-opponent-logo">
																<span class="match-histories-item-opponent-name text-of">G2 Esports</span>

							</div>
							<div class="match-histories-item-date">
								2025/02/27							</div>
						</a>
									
																	<a href="/449000/drx-vs-team-vitality-champions-tour-2025-masters-bangkok-r2-1-0" class="match-histories-item wf-module-item  mod-win">
							
							<div class="match-histories-item-result mod-win">
								<span class="rf">2</span>
								<span class="ra">1</span>
							</div> 
							<div class="match-histories-item-opponent" style="min-width: 0;">
								<span style="font-style: italic;">vs.</span>

																	<img src="//owcdn.net/img/63b17abd77fc0.png" class="match-histories-item-opponent-logo">
																<span class="match-histories-item-opponent-name text-of">DRX</span>

							</div>
							<div class="match-histories-item-date">
								2025/02/22							</div>
						</a>
									
																	<a href="/448599/team-vitality-vs-t1-champions-tour-2025-masters-bangkok-r1" class="match-histories-item wf-module-item  mod-win">
							
							<div class="match-histories-item-result mod-win">
								<span class="rf">2</span>
								<span class="ra">0</span>
							</div> 
							<div class="match-histories-item-opponent" style="min-width: 0;">
								<span style="font-style: italic;">vs.</span>

																	<img src="//owcdn.net/img/62fe0b8f6b084.png" class="match-histories-item-opponent-logo">
																<span class="match-histories-item-opponent-name text-of">T1</span>

							</div>
							<div class="match-histories-item-date">
								2025/02/21							</div>
						</a>
									
																	<a href="/429390/team-vitality-vs-team-liquid-champions-tour-2025-emea-kickoff-gf" class="match-histories-item wf-module-item  mod-win">
							
							<div class="match-histories-item-result mod-win">
								<span class="rf">3</span>
								<span class="ra">2</span>
							</div> 
							<div class="match-histories-item-opponent" style="min-width: 0;">
								<span style="font-style: italic;">vs.</span>

																	<img src="//owcdn.net/img/640c381f0603f.png" class="match-histories-item-opponent-logo">
																<span class="match-histories-item-opponent-name text-of">Team Liquid</span>

							</div>
							<div class="match-histories-item-date">
								2025/02/09							</div>
						</a>
									
																	<a href="/429389/team-vitality-vs-team-heretics-champions-tour-2025-emea-kickoff-ubf" class="match-histories-item wf-module-item  mod-win">
							
							<div class="match-histories-item-result mod-win">
								<span class="rf">2</span>
								<span class="ra">0</span>
							</div> 
							<div class="match-histories-item-opponent" style="min-width: 0;">
								<span style="font-style: italic;">vs.</span>

																	<img src="//owcdn.net/img/637b755224c12.png" class="match-histories-item-opponent-logo">
																<span class="match-histories-item-opponent-name text-of">Team Heretics</span>

							</div>
							<div class="match-histories-item-date">
								2025/02/07							</div>
						</a>
									
			</div>
			</div>


<div class="noselect" style="display: flex; margin: 22px 0; justify-content: space-between;">

	<div style="display: flex; padding-left: 25px; align-items: center;">
		<div class="wf-label comments-label" style="margin-right: 12px; padding: 0;">Comments:</div>

		<div id="comments" style="margin-top: -82px;"></div>

									<a href="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1/?pmt=1#comments" class="btn mod-action pmt-btn" style="margin-right: 20px;">Hide Pre-match</a>
					
		<div class="btn-group">
							<span>
					Threaded
				</span>
				<a href="/449012/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1/?view=linear#comments">
					Linear
				</a>
					</div>



		
	</div>



	<div>
		<a class="btn mod-page mod-to-bottom" href="#bottom">
			<i class="fa fa-chevron-down"></i>
		</a>
	</div>
</div><div class="post-container" data-auto-scroll="0">
	<div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4569097">
		<a id="1" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#1</div>
			
			<i class="post-header-flag flag mod-bj" title="Benin"></i> 
			<a href="/user/iTzJ4son" class="post-header-author  mod-vlr">
				iTzJ4son			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4569097" data-frag-status="neutral">
					<div class="post-frag-count positive">
						50 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Steel and Hiko both drop 40</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 15, 2025 at 10:23 PM IST">
					 2 weeks ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4569097" data-author-name="iTzJ4son">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4569097">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4569097/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="1">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4569097"></div>
		<div class="reply-form" data-post-id="4569097"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4619631">
		<a id="31" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#31</div>
			
			<i class="post-header-flag flag mod-vn" title="Vietnam"></i> 
			<a href="/user/yungzico" class="post-header-author  mod-vlr">
				yungzico			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/624/paper-rex"><img class="post-header-flair" src="//owcdn.net/img/62bbebb185a7e.png" title="Paper Rex"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4619631" data-frag-status="neutral">
					<div class="post-frag-count positive">
						5 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>then brax, skad, and n0thing are subbed and drop 130 individually </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 4:56 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4619631" data-author-name="yungzico">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4619631">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4619631/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="31">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4619631"></div>
		<div class="reply-form" data-post-id="4619631"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4621060">
		<a id="138" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#138</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/mads10" class="post-header-author  mod-vlr">
				mads10			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621060" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>W xD</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:15 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621060" data-author-name="mads10">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621060">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621060/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="138">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621060"></div>
		<div class="reply-form" data-post-id="4621060"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4619793">
		<a id="33" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#33</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/vasswood" class="post-header-author  mod-vlr">
				vasswood			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/17/gen-g"><img class="post-header-flair" src="//owcdn.net/img/662f72041aff8.png" title="Gen.G"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4619793" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-3 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>:3</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 5:13 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4619793" data-author-name="vasswood">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4619793">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4619793/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="33">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4619793"></div>
		<div class="reply-form" data-post-id="4619793"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620703">
		<a id="104" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#104</div>
			
			<i class="post-header-flag flag mod-cz" title="Czech Republic"></i> 
			<a href="/user/STEWIK" class="post-header-author  mod-vlr">
				STEWIK			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/120/100-thieves"><img class="post-header-flair" src="//owcdn.net/img/603c00dbb7d39.png" title="100 Thieves"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620703" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>God I wish</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:39 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620703" data-author-name="STEWIK">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620703">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620703/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="104">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620703"></div>
		<div class="reply-form" data-post-id="4620703"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4576654">
		<a id="2" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#2</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/cameran" class="post-header-author  mod-vlr">
				cameran			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/2/sentinels"><img class="post-header-flair" src="//owcdn.net/img/62875027c8e06.png" title="Sentinels"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4576654" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-4 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>G2  2-0 t1</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 19, 2025 at 2:43 AM IST">
					 1 week ago				</span>
									&sdot;
					<span class="post-edit">
						edited <span class="js-date-toggle" title="Feb 25, 2025 at 12:58 AM IST">6 days ago</span>
					</span>

				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4576654" data-author-name="cameran">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4576654">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4576654/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="2">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4576654"></div>
		<div class="reply-form" data-post-id="4576654"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4586809">
		<a id="3" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#3</div>
			
			<i class="post-header-flag flag mod-cn" title="China"></i> 
			<a href="/user/fungame024" class="post-header-author  mod-vlr">
				fungame024			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/12685/trace-esports"><img class="post-header-flair" src="//owcdn.net/img/6433a2d3b58c9.png" title="Trace Esports"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4586809" data-frag-status="neutral">
					<div class="post-frag-count positive">
						10 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>TBD 2-0 TBD</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 21, 2025 at 12:26 PM IST">
					 1 week ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4586809" data-author-name="fungame024">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4586809">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4586809/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="3">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4586809"></div>
		<div class="reply-form" data-post-id="4586809"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4605925">
		<a id="4" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#4</div>
			
			<i class="post-header-flag flag mod-vn" title="Vietnam"></i> 
			<a href="/user/Bluez" class="post-header-author  mod-vlr">
				Bluez			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/2/sentinels"><img class="post-header-flair" src="//owcdn.net/img/62875027c8e06.png" title="Sentinels"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4605925" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-4 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>G2 2-1 T1 </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 24, 2025 at 7:27 PM IST">
					 6 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4605925" data-author-name="Bluez">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4605925">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4605925/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="4">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4605925"></div>
		<div class="reply-form" data-post-id="4605925"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4606758">
		<a id="5" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#5</div>
			
			<i class="post-header-flag flag mod-jp" title="Japan"></i> 
			<a href="/user/nanashitokumei111" class="post-header-author  mod-vlr">
				nanashitokumei111			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/2934/fennel"><img class="post-header-flair" src="//owcdn.net/img/60d398671c682.png" title="FENNEL"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4606758" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>T1 0-2 G2</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 24, 2025 at 10:41 PM IST">
					 6 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4606758" data-author-name="nanashitokumei111">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4606758">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4606758/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="5">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4606758"></div>
		<div class="reply-form" data-post-id="4606758"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4613964">
		<a id="6" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#6</div>
			
			<i class="post-header-flag flag mod-en" title="England"></i> 
			<a href="/user/Azzelastia" class="post-header-author  mod-vlr">
				Azzelastia			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/6675/the-guard"><img class="post-header-flair" src="//owcdn.net/img/649d272e6ef32.png" title="The Guard"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4613964" data-frag-status="neutral">
					<div class="post-frag-count positive">
						8 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>T1 2-0 VIT</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 3:42 PM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4613964" data-author-name="Azzelastia">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4613964">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4613964/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="6">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4613964"></div>
		<div class="reply-form" data-post-id="4613964"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4621057">
		<a id="137" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#137</div>
			
			<i class="post-header-flag flag mod-ph" title="Philippines"></i> 
			<a href="/user/Frogco" class="post-header-author  mod-vlr">
				Frogco			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621057" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>u cooked</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:15 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621057" data-author-name="Frogco">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621057">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621057/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="137">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621057"></div>
		<div class="reply-form" data-post-id="4621057"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4621895">
		<a id="171" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#171</div>
			
			<i class="post-header-flag flag mod-kr" title="South Korea"></i> 
			<a href="/user/posylicker" class="post-header-author  mod-vlr">
				posylicker			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/17/gen-g"><img class="post-header-flair" src="//owcdn.net/img/662f72041aff8.png" title="Gen.G"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621895" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>close enough</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 9:15 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621895" data-author-name="posylicker">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621895">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621895/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="171">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621895"></div>
		<div class="reply-form" data-post-id="4621895"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4615071">
		<a id="7" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#7</div>
			
			<i class="post-header-flag flag mod-kr" title="South Korea"></i> 
			<a href="/user/ButterflyEffect23" class="post-header-author  mod-vlr">
				ButterflyEffect23			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/14/t1"><img class="post-header-flair" src="//owcdn.net/img/62fe0b8f6b084.png" title="T1"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4615071" data-frag-status="neutral">
					<div class="post-frag-count positive">
						5 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>#T1Fighting</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 6:27 PM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4615071" data-author-name="ButterflyEffect23">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4615071">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4615071/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="7">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4615071"></div>
		<div class="reply-form" data-post-id="4615071"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4615247">
		<a id="8" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#8</div>
			
			<i class="post-header-flag flag mod-id" title="Indonesia"></i> 
			<a href="/user/mokyoxx" class="post-header-author  mod-vlr">
				mokyoxx			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4615247" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>t1 2-0 g2</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 6:39 PM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4615247" data-author-name="mokyoxx">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4615247">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4615247/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="8">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4615247"></div>
		<div class="reply-form" data-post-id="4615247"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4615998">
		<a id="9" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#9</div>
			
			<i class="post-header-flag flag mod-es" title="Spain"></i> 
			<a href="/user/SuPerLeLe" class="post-header-author  mod-vlr">
				SuPerLeLe			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/11981/dragon-ranger-gaming"><img class="post-header-flair" src="//owcdn.net/img/642233fc01f26.png" title="Dragon Ranger Gaming"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4615998" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-10 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>vit</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 8:02 PM IST">
					 3 days ago				</span>
									&sdot;
					<span class="post-edit">
						edited <span class="js-date-toggle" title="Feb 28, 2025 at 8:16 PM IST">2 days ago</span>
					</span>

				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4615998" data-author-name="SuPerLeLe">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4615998">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4615998/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="9">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4615998"></div>
		<div class="reply-form" data-post-id="4615998"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4616481">
		<a id="10" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#10</div>
			
			<i class="post-header-flag flag mod-cn" title="China"></i> 
			<a href="/user/lollipop_on_twitter" class="post-header-author  mod-vlr">
				lollipop_on_twitter			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4616481" data-frag-status="neutral">
					<div class="post-frag-count positive">
						3 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>t1 wins</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 9:04 PM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4616481" data-author-name="lollipop_on_twitter">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4616481">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4616481/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="10">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4616481"></div>
		<div class="reply-form" data-post-id="4616481"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4616530">
		<a id="11" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#11</div>
			
			<i class="post-header-flag flag mod-vi" title="Virgin Islands, U.S."></i> 
			<a href="/user/Anzaldinho" class="post-header-author  mod-vlr">
				Anzaldinho			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4616530" data-frag-status="neutral">
					<div class="post-frag-count positive">
						5 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>T1 2-1</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 9:07 PM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4616530" data-author-name="Anzaldinho">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4616530">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4616530/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="11">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4616530"></div>
		<div class="reply-form" data-post-id="4616530"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4621583">
		<a id="166" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#166</div>
			
			<i class="post-header-flag flag mod-ua" title="Ukraine"></i> 
			<a href="/user/freakymonkey67" class="post-header-author  mod-vlr">
				freakymonkey67			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621583" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>damn </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:43 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621583" data-author-name="freakymonkey67">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621583">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621583/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="166">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621583"></div>
		<div class="reply-form" data-post-id="4621583"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4621590">
		<a id="167" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#167</div>
			
			<i class="post-header-flag flag mod-vi" title="Virgin Islands, U.S."></i> 
			<a href="/user/Anzaldinho" class="post-header-author  mod-vlr">
				Anzaldinho			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621590" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>should've been 2-1 for edg too if you ask me</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:44 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621590" data-author-name="Anzaldinho">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621590">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621590/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="167">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621590"></div>
		<div class="reply-form" data-post-id="4621590"></div>
	</div>
</div></div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4616548">
		<a id="12" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#12</div>
			
			<i class="post-header-flag flag mod-in" title="India"></i> 
			<a href="/user/Jarvuy" class="post-header-author  mod-vlr">
				Jarvuy			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/2/sentinels"><img class="post-header-flair" src="//owcdn.net/img/62875027c8e06.png" title="Sentinels"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4616548" data-frag-status="neutral">
					<div class="post-frag-count positive">
						28 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>T1 exposing these frauds tomorrow. Hope VIT has the flight tickets ready 😔</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 9:09 PM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4616548" data-author-name="Jarvuy">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4616548">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4616548/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="12">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4616548"></div>
		<div class="reply-form" data-post-id="4616548"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4616620">
		<a id="13" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#13</div>
			
			<i class="post-header-flag flag mod-nl" title="Netherlands"></i> 
			<a href="/user/Bigfish" class="post-header-author  mod-vlr">
				Bigfish			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4616620" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-8 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Lol t1 def going home</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 9:16 PM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4616620" data-author-name="Bigfish">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4616620">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4616620/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="13">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4616620"></div>
		<div class="reply-form" data-post-id="4616620"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4619800">
		<a id="34" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#34</div>
			
			<i class="post-header-flag flag mod-id" title="Indonesia"></i> 
			<a href="/user/Coolkas" class="post-header-author  mod-vlr">
				Coolkas			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/13565/3"><img class="post-header-flair" src="//owcdn.net/img/6519caa187408.png" title=":3"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4619800" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Whoever lost is watching grandfinal at venue, so both teams going home </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 5:13 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4619800" data-author-name="Coolkas">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4619800">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4619800/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="34">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4619800"></div>
		<div class="reply-form" data-post-id="4619800"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4621144">
		<a id="149" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#149</div>
			
			<i class="post-header-flag flag mod-eu" title="Europe"></i> 
			<a href="/user/1swarm" class="post-header-author  mod-vlr">
				1swarm			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/188/cloud9"><img class="post-header-flair" src="//owcdn.net/img/628addcbd509e.png" title="Cloud9"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621144" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>well well well</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:18 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621144" data-author-name="1swarm">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621144">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621144/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="149">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621144"></div>
		<div class="reply-form" data-post-id="4621144"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-3" data-post-id="4621953">
		<a id="172" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#172</div>
			
			<i class="post-header-flag flag mod-nl" title="Netherlands"></i> 
			<a href="/user/Bigfish" class="post-header-author  mod-vlr">
				Bigfish			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621953" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>But what does this mean for c9?</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 9:25 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621953" data-author-name="Bigfish">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621953">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621953/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="172">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621953"></div>
		<div class="reply-form" data-post-id="4621953"></div>
	</div>
</div></div></div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4616626">
		<a id="14" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#14</div>
			
			<i class="post-header-flag flag mod-in" title="India"></i> 
			<a href="/user/gut5" class="post-header-author  mod-vlr">
				gut5			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4616626" data-frag-status="neutral">
					<div class="post-frag-count positive">
						2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>if vit win map toss vit wins otherwise T1 ezz</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 9:17 PM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4616626" data-author-name="gut5">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4616626">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4616626/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="14">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4616626"></div>
		<div class="reply-form" data-post-id="4616626"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4616627">
		<a id="15" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#15</div>
			
			<i class="post-header-flag flag mod-ps" title="Palestine"></i> 
			<a href="/user/z12" class="post-header-author  mod-vlr">
				z12			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/11058/g2-esports"><img class="post-header-flair" src="//owcdn.net/img/633822848a741.png" title="G2 Esports"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4616627" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>the real superteam shall prevail ahh</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 9:17 PM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4616627" data-author-name="z12">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4616627">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4616627/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="15">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4616627"></div>
		<div class="reply-form" data-post-id="4616627"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4622731">
		<a id="175" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#175</div>
			
			<i class="post-header-flag flag mod-ps" title="Palestine"></i> 
			<a href="/user/z12" class="post-header-author  mod-vlr">
				z12			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/11058/g2-esports"><img class="post-header-flair" src="//owcdn.net/img/633822848a741.png" title="G2 Esports"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4622731" data-frag-status="neutral">
					<div class="post-frag-count positive">
						2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>the real superteam did prevail fuck off botality </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Mar 1, 2025 at 1:09 AM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4622731" data-author-name="z12">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4622731">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4622731/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="175">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4622731"></div>
		<div class="reply-form" data-post-id="4622731"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4616653">
		<a id="16" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#16</div>
			
			<i class="post-header-flag flag mod-al" title="Albania"></i> 
			<a href="/user/imcarpe" class="post-header-author  mod-vlr">
				imcarpe			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4616653" data-frag-status="neutral">
					<div class="post-frag-count positive">
						7 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>i think VIT is broken ( t1 win) </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 9:20 PM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4616653" data-author-name="imcarpe">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4616653">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4616653/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="16">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4616653"></div>
		<div class="reply-form" data-post-id="4616653"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4616700">
		<a id="17" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#17</div>
			
			<i class="post-header-flag flag mod-un" title="International"></i> 
			<a href="/user/Compact665" class="post-header-author  mod-vlr">
				Compact665			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4616700" data-frag-status="neutral">
					<div class="post-frag-count positive">
						2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>T2-0 VIT</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 9:29 PM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4616700" data-author-name="Compact665">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4616700">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4616700/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="17">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4616700"></div>
		<div class="reply-form" data-post-id="4616700"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4616782">
		<a id="18" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#18</div>
			
			<i class="post-header-flag flag mod-pl" title="Poland"></i> 
			<a href="/user/tong5" class="post-header-author  mod-vlr">
				tong5			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/474/team-liquid"><img class="post-header-flair" src="//owcdn.net/img/640c38262824c.png" title="Team Liquid"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4616782" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-3 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>classic upper bracket throw ez Vita champs</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 9:44 PM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4616782" data-author-name="tong5">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4616782">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4616782/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="18">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4616782"></div>
		<div class="reply-form" data-post-id="4616782"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4623803">
		<a id="179" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#179</div>
			
			<i class="post-header-flag flag mod-ph" title="Philippines"></i> 
			<a href="/user/Fendy1" class="post-header-author  mod-vlr">
				Fendy1			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4623803" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>delusional polish</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Mar 1, 2025 at 12:58 PM IST">
					 1 day ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4623803" data-author-name="Fendy1">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4623803">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4623803/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="179">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4623803"></div>
		<div class="reply-form" data-post-id="4623803"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4617163">
		<a id="19" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#19</div>
			
			<i class="post-header-flag flag mod-in" title="India"></i> 
			<a href="/user/TaniBoy7" class="post-header-author  mod-vlr">
				TaniBoy7			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/2/sentinels"><img class="post-header-flair" src="//owcdn.net/img/62875027c8e06.png" title="Sentinels"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4617163" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>VIT 2-1 I suspect atleast 1 map going to OT and the match being very close</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 27, 2025 at 11:28 PM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4617163" data-author-name="TaniBoy7">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4617163">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4617163/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="19">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4617163"></div>
		<div class="reply-form" data-post-id="4617163"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4617292">
		<a id="20" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#20</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/Anoymouse" class="post-header-author  mod-vlr">
				Anoymouse			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/6961/loud"><img class="post-header-flair" src="//owcdn.net/img/62bbec8dc1b9f.png" title="LOUD"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4617292" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Vit2-0 easily again </p>
<p>#mvgs</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 12:17 AM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4617292" data-author-name="Anoymouse">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4617292">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4617292/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="20">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4617292"></div>
		<div class="reply-form" data-post-id="4617292"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4617374">
		<a id="21" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#21</div>
			
			<i class="post-header-flag flag mod-nz" title="New Zealand"></i> 
			<a href="/user/Tobiiverse" class="post-header-author  mod-vlr">
				Tobiiverse			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/6530/g2-gozen"><img class="post-header-flair" src="//owcdn.net/img/633822848a741.png" title="G2 Gozen"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4617374" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Vit wins but please cause the upset T1🙏🙏🙏</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 12:51 AM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4617374" data-author-name="Tobiiverse">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4617374">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4617374/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="21">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4617374"></div>
		<div class="reply-form" data-post-id="4617374"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4617664">
		<a id="22" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#22</div>
			
			<i class="post-header-flag flag mod-es" title="Spain"></i> 
			<a href="/user/elpolli777" class="post-header-author  mod-vlr">
				elpolli777			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4617664" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Pls vit win this match for emea</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 2:44 AM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4617664" data-author-name="elpolli777">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4617664">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4617664/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="22">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4617664"></div>
		<div class="reply-form" data-post-id="4617664"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4623807">
		<a id="180" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#180</div>
			
			<i class="post-header-flag flag mod-ph" title="Philippines"></i> 
			<a href="/user/Fendy1" class="post-header-author  mod-vlr">
				Fendy1			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4623807" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>fraud region</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Mar 1, 2025 at 12:59 PM IST">
					 1 day ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4623807" data-author-name="Fendy1">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4623807">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4623807/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="180">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4623807"></div>
		<div class="reply-form" data-post-id="4623807"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4617842">
		<a id="23" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#23</div>
			
			<i class="post-header-flag flag mod-ar" title="Argentina"></i> 
			<a href="/user/Uragirimono19" class="post-header-author  mod-vlr">
				Uragirimono19			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/2355/kr-esports"><img class="post-header-flair" src="//owcdn.net/img/63976677069e1.png" title="KRÜ Esports"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4617842" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>t1 2-1</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 4:00 AM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4617842" data-author-name="Uragirimono19">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4617842">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4617842/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="23">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4617842"></div>
		<div class="reply-form" data-post-id="4617842"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4618244">
		<a id="24" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#24</div>
			
			<i class="post-header-flag flag mod-lv" title="Latvia"></i> 
			<a href="/user/johnlenin" class="post-header-author  mod-vlr">
				johnlenin			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/8185/drx"><img class="post-header-flair" src="//owcdn.net/img/63b17ac3a7d00.png" title="DRX"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4618244" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>ez for bookies and betting mafia 👌<br />
prepare your money 🤑</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:31 AM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4618244" data-author-name="johnlenin">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4618244">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4618244/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="24">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4618244"></div>
		<div class="reply-form" data-post-id="4618244"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4618506">
		<a id="25" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#25</div>
			
			<i class="post-header-flag flag mod-tr" title="Turkey"></i> 
			<a href="/user/-Artorias" class="post-header-author  mod-vlr">
				-Artorias			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/1184/fut-esports"><img class="post-header-flair" src="//owcdn.net/img/632be99c96c64.png" title="FUT Esports"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4618506" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>t1 clears </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:36 AM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4618506" data-author-name="-Artorias">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4618506">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4618506/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="25">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4618506"></div>
		<div class="reply-form" data-post-id="4618506"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4618606">
		<a id="26" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#26</div>
			
			<i class="post-header-flag flag mod-vn" title="Vietnam"></i> 
			<a href="/user/Zeron" class="post-header-author  mod-vlr">
				Zeron			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/11981/dragon-ranger-gaming"><img class="post-header-flair" src="//owcdn.net/img/642233fc01f26.png" title="Dragon Ranger Gaming"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4618606" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>I got a bad feeling about this matchup but fuck it VIT 2-1</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:21 AM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4618606" data-author-name="Zeron">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4618606">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4618606/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="26">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4618606"></div>
		<div class="reply-form" data-post-id="4618606"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4618626">
		<a id="27" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#27</div>
			
			<i class="post-header-flag flag mod-ca" title="Canada"></i> 
			<a href="/user/destroylonely" class="post-header-author  mod-vlr">
				destroylonely			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/11058/g2-esports"><img class="post-header-flair" src="//owcdn.net/img/633822848a741.png" title="G2 Esports"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4618626" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>t1 revenge </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:31 AM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4618626" data-author-name="destroylonely">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4618626">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4618626/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="27">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4618626"></div>
		<div class="reply-form" data-post-id="4618626"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4618657">
		<a id="28" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#28</div>
			
			<i class="post-header-flag flag mod-id" title="Indonesia"></i> 
			<a href="/user/Kudryavka" class="post-header-author  mod-vlr">
				Kudryavka			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/13565/3"><img class="post-header-flair" src="//owcdn.net/img/6519caa187408.png" title=":3"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4618657" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>another sylvan ace clutch masterclass</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:45 AM IST">
					 3 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4618657" data-author-name="Kudryavka">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4618657">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4618657/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="28">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4618657"></div>
		<div class="reply-form" data-post-id="4618657"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4619468">
		<a id="29" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#29</div>
			
			<i class="post-header-flag flag mod-th" title="Thailand"></i> 
			<a href="/user/PTzGM" class="post-header-author  mod-vlr">
				PTzGM			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4619468" data-frag-status="neutral">
					<div class="post-frag-count positive">
						2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>T1 2-1</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 4:26 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4619468" data-author-name="PTzGM">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4619468">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4619468/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="29">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4619468"></div>
		<div class="reply-form" data-post-id="4619468"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4619612">
		<a id="30" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#30</div>
			
			<i class="post-header-flag flag mod-ve" title="Venezuela"></i> 
			<a href="/user/Jajajajajajjah" class="post-header-author  mod-vlr">
				Jajajajajajjah			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4619612" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>t1 26-2</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 4:54 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4619612" data-author-name="Jajajajajajjah">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4619612">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4619612/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="30">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4619612"></div>
		<div class="reply-form" data-post-id="4619612"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4619779">
		<a id="32" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#32</div>
			
			<i class="post-header-flag flag mod-id" title="Indonesia"></i> 
			<a href="/user/Coolkas" class="post-header-author  mod-vlr">
				Coolkas			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/13565/3"><img class="post-header-flair" src="//owcdn.net/img/6519caa187408.png" title=":3"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4619779" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>T1 kadang busuk kadang dewa</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 5:12 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4619779" data-author-name="Coolkas">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4619779">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4619779/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="32">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4619779"></div>
		<div class="reply-form" data-post-id="4619779"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4619930">
		<a id="35" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#35</div>
			
			<i class="post-header-flag flag mod-lv" title="Latvia"></i> 
			<a href="/user/johnlenin" class="post-header-author  mod-vlr">
				johnlenin			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/8185/drx"><img class="post-header-flair" src="//owcdn.net/img/63b17ac3a7d00.png" title="DRX"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4619930" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Vita 2-0<br />
ez script</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 5:23 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4619930" data-author-name="johnlenin">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4619930">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4619930/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="35">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4619930"></div>
		<div class="reply-form" data-post-id="4619930"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620001">
		<a id="36" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#36</div>
			
			<i class="post-header-flag flag mod-cn" title="China"></i> 
			<a href="/user/lollipop_on_twitter" class="post-header-author  mod-vlr">
				lollipop_on_twitter			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620001" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>t1 2-0</p>
<p>generational upset</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 5:30 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620001" data-author-name="lollipop_on_twitter">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620001">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620001/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="36">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620001"></div>
		<div class="reply-form" data-post-id="4620001"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620064">
		<a id="37" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#37</div>
			
			<i class="post-header-flag flag mod-eu" title="Europe"></i> 
			<a href="/user/Neon__" class="post-header-author  mod-vlr">
				Neon__			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620064" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-4 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Please change pansy into someone else. Id rather listen to someone random streamer than her to cast this game, i don't wanna hear no bias or moaning at casting when insane moments are happening.</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 5:38 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620064" data-author-name="Neon__">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620064">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620064/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="37">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620064"></div>
		<div class="reply-form" data-post-id="4620064"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620096">
		<a id="38" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#38</div>
			
			<i class="post-header-flag flag mod-cn" title="China"></i> 
			<a href="/user/withsn" class="post-header-author  mod-vlr">
				withsn			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620096" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>guess riot have to balance the caster gender</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 5:43 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620096" data-author-name="withsn">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620096">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620096/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="38">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620096"></div>
		<div class="reply-form" data-post-id="4620096"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4620099">
		<a id="39" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#39</div>
			
			<i class="post-header-flag flag mod-eu" title="Europe"></i> 
			<a href="/user/Neon__" class="post-header-author  mod-vlr">
				Neon__			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620099" data-frag-status="neutral">
					<div class="post-frag-count positive">
						2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>ngl bro im not sexist or what but if they gonna put a female caster at least make it someone who is not blatantly bias and also not moaning every 3 seconds on the casting jeez.</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 5:45 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620099" data-author-name="Neon__">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620099">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620099/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="39">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620099"></div>
		<div class="reply-form" data-post-id="4620099"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-3" data-post-id="4620337">
		<a id="65" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#65</div>
			
			<i class="post-header-flag flag mod-cn" title="China"></i> 
			<a href="/user/withsn" class="post-header-author  mod-vlr">
				withsn			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620337" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>i have watched some of game changer game, as far as i consider, i got to tell u most of these caster have the some little bad habit like her, like they didnt focus on game itself or suddenly start to shut loudly. in that case i think she is the best choice they can pick for.</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:38 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620337" data-author-name="withsn">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620337">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620337/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="65">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620337"></div>
		<div class="reply-form" data-post-id="4620337"></div>
	</div>
</div></div></div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620120">
		<a id="40" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#40</div>
			
			<i class="post-header-flag flag mod-gb" title="United Kingdom"></i> 
			<a href="/user/sugaclutch" class="post-header-author  mod-vlr">
				sugaclutch			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620120" data-frag-status="neutral">
					<div class="post-frag-count positive">
						4 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>t1 2-0 that fraud superteam...vitality wont win a shit wo proper igl</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 5:51 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620120" data-author-name="sugaclutch">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620120">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620120/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="40">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620120"></div>
		<div class="reply-form" data-post-id="4620120"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620144">
		<a id="43" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#43</div>
			
			<i class="post-header-flag flag mod-pl" title="Poland"></i> 
			<a href="/user/Apaqt" class="post-header-author  mod-vlr">
				Apaqt			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620144" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-3 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Sat on TH lmfao btw they won Kickoff unlike a certain team last year ahmm</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 5:56 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620144" data-author-name="Apaqt">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620144">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620144/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="43">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620144"></div>
		<div class="reply-form" data-post-id="4620144"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4620167">
		<a id="44" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#44</div>
			
			<i class="post-header-flag flag mod-gb" title="United Kingdom"></i> 
			<a href="/user/sugaclutch" class="post-header-author  mod-vlr">
				sugaclutch			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620167" data-frag-status="neutral">
					<div class="post-frag-count positive">
						2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>th carried ur ass in 2024...don forget ur father son<br />
lmao if winning kickoff is an achievement...fnc fans should talk their shit not u kekw </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:03 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620167" data-author-name="sugaclutch">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620167">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620167/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="44">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620167"></div>
		<div class="reply-form" data-post-id="4620167"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-3" data-post-id="4620185">
		<a id="45" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#45</div>
			
			<i class="post-header-flag flag mod-pl" title="Poland"></i> 
			<a href="/user/Apaqt" class="post-header-author  mod-vlr">
				Apaqt			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620185" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Can't win shit Can't make events having a Cinderella year doesn't mean shit kid </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:07 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620185" data-author-name="Apaqt">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620185">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620185/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="45">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620185"></div>
		<div class="reply-form" data-post-id="4620185"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-4" data-post-id="4620191">
		<a id="46" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#46</div>
			
			<i class="post-header-flag flag mod-gb" title="United Kingdom"></i> 
			<a href="/user/sugaclutch" class="post-header-author  mod-vlr">
				sugaclutch			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620191" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>enjoy the 0-2... take the L<br />
we will see in next 2 tournament</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:08 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620191" data-author-name="sugaclutch">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620191">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620191/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="46">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620191"></div>
		<div class="reply-form" data-post-id="4620191"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-5" data-post-id="4620335">
		<a id="64" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#64</div>
			
			<i class="post-header-flag flag mod-eu" title="Europe"></i> 
			<a href="/user/kekW_gaming" class="post-header-author  mod-vlr">
				kekW_gaming			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620335" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>TH getting rekt on Scrims btw. They're disbanding after this year. They won't even make it to the next tournaments . Getting 3-0ed by Lulquid btw KEKW</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:38 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620335" data-author-name="kekW_gaming">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620335">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620335/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="64">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620335"></div>
		<div class="reply-form" data-post-id="4620335"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-5" data-post-id="4620361">
		<a id="70" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#70</div>
			
			<i class="post-header-flag flag mod-pl" title="Poland"></i> 
			<a href="/user/Apaqt" class="post-header-author  mod-vlr">
				Apaqt			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620361" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Kkkew vit comeback and TH not even present</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:41 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620361" data-author-name="Apaqt">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620361">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620361/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="70">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620361"></div>
		<div class="reply-form" data-post-id="4620361"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-6" data-post-id="4620837">
		<a id="117" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#117</div>
			
			<i class="post-header-flag flag mod-gb" title="United Kingdom"></i> 
			<a href="/user/sugaclutch" class="post-header-author  mod-vlr">
				sugaclutch			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620837" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>8-2 btw </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:58 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620837" data-author-name="sugaclutch">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620837">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620837/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="117">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620837"></div>
		<div class="reply-form" data-post-id="4620837"></div>
	</div>
</div></div></div></div></div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620235">
		<a id="49" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#49</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/Bot_teams" class="post-header-author  mod-vlr">
				Bot_teams			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620235" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>jinxed Vit 2-0</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:22 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620235" data-author-name="Bot_teams">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620235">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620235/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="49">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620235"></div>
		<div class="reply-form" data-post-id="4620235"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620138">
		<a id="41" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#41</div>
			
			<i class="post-header-flag flag mod-br" title="Brazil"></i> 
			<a href="/user/Amadeus11" class="post-header-author  mod-vlr">
				Amadeus11			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620138" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>won pistol round then lose all the next rounds. nice strategy Vit lol</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 5:55 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620138" data-author-name="Amadeus11">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620138">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620138/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="41">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620138"></div>
		<div class="reply-form" data-post-id="4620138"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620394">
		<a id="76" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#76</div>
			
			<i class="post-header-flag flag mod-cn" title="China"></i> 
			<a href="/user/withsn" class="post-header-author  mod-vlr">
				withsn			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620394" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>same for t1 on second half, only they win the antieco.</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:45 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620394" data-author-name="withsn">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620394">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620394/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="76">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620394"></div>
		<div class="reply-form" data-post-id="4620394"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620142">
		<a id="42" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#42</div>
			
			<i class="post-header-flag flag mod-fr" title="France"></i> 
			<a href="/user/DreeLa" class="post-header-author  mod-vlr">
				DreeLa			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/2059/team-vitality"><img class="post-header-flair" src="//owcdn.net/img/6466d7936fd86.png" title="Team Vitality"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620142" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Vita win </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 5:55 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620142" data-author-name="DreeLa">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620142">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620142/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="42">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620142"></div>
		<div class="reply-form" data-post-id="4620142"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620226">
		<a id="47" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#47</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/Bot_teams" class="post-header-author  mod-vlr">
				Bot_teams			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620226" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-8 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>t1 can't win against real tier 1 team</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:19 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620226" data-author-name="Bot_teams">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620226">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620226/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="47">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620226"></div>
		<div class="reply-form" data-post-id="4620226"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620228">
		<a id="48" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#48</div>
			
			<i class="post-header-flag flag mod-in" title="India"></i> 
			<a href="/user/badger252" class="post-header-author  mod-vlr">
				badger252			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/120/100-thieves"><img class="post-header-flair" src="//owcdn.net/img/603c00dbb7d39.png" title="100 Thieves"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620228" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>10-4 throw is crazy</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:19 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620228" data-author-name="badger252">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620228">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620228/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="48">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620228"></div>
		<div class="reply-form" data-post-id="4620228"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620242">
		<a id="50" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#50</div>
			
			<i class="post-header-flag flag mod-ve" title="Venezuela"></i> 
			<a href="/user/Jajajajajajjah" class="post-header-author  mod-vlr">
				Jajajajajajjah			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620242" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>choke1?????</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:23 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620242" data-author-name="Jajajajajajjah">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620242">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620242/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="50">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620242"></div>
		<div class="reply-form" data-post-id="4620242"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620251">
		<a id="51" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#51</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/PoRest0ranam" class="post-header-author  mod-vlr">
				PoRest0ranam			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620251" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Another choke from T1, why this keeps happening...</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:26 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620251" data-author-name="PoRest0ranam">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620251">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620251/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="51">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620251"></div>
		<div class="reply-form" data-post-id="4620251"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620262">
		<a id="52" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#52</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/PoRest0ranam" class="post-header-author  mod-vlr">
				PoRest0ranam			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620262" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Ot after 7 1<br />
Ok boys</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:32 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620262" data-author-name="PoRest0ranam">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620262">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620262/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="52">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620262"></div>
		<div class="reply-form" data-post-id="4620262"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620268">
		<a id="54" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#54</div>
			
			<i class="post-header-flag flag mod-in" title="India"></i> 
			<a href="/user/badger252" class="post-header-author  mod-vlr">
				badger252			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/120/100-thieves"><img class="post-header-flair" src="//owcdn.net/img/603c00dbb7d39.png" title="100 Thieves"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620268" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>10 4*</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:34 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620268" data-author-name="badger252">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620268">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620268/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="54">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620268"></div>
		<div class="reply-form" data-post-id="4620268"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620267">
		<a id="53" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#53</div>
			
			<i class="post-header-flag flag mod-kr" title="South Korea"></i> 
			<a href="/user/shinehh" class="post-header-author  mod-vlr">
				shinehh			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/8185/drx"><img class="post-header-flair" src="//owcdn.net/img/63b17ac3a7d00.png" title="DRX"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620267" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Please please please -autumn before regular season</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:34 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620267" data-author-name="shinehh">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620267">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620267/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="53">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620267"></div>
		<div class="reply-form" data-post-id="4620267"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620355">
		<a id="68" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#68</div>
			
			<i class="post-header-flag flag mod-pl" title="Poland"></i> 
			<a href="/user/Apaqt" class="post-header-author  mod-vlr">
				Apaqt			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620355" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Frr how tf autumn still in tier 1 blud doesn't even know which player should play a match and which should be benched</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:40 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620355" data-author-name="Apaqt">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620355">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620355/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="68">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620355"></div>
		<div class="reply-form" data-post-id="4620355"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620288">
		<a id="55" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#55</div>
			
			<i class="post-header-flag flag mod-eu" title="Europe"></i> 
			<a href="/user/Neon__" class="post-header-author  mod-vlr">
				Neon__			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620288" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Generational choke holy moly thank you for odds 5.42  at 10-6 XDDDD</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:36 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620288" data-author-name="Neon__">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620288">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620288/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="55">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620288"></div>
		<div class="reply-form" data-post-id="4620288"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620290">
		<a id="56" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#56</div>
			
			<i class="post-header-flag flag mod-ng" title="Nigeria"></i> 
			<a href="/user/sayjin" class="post-header-author  mod-vlr">
				sayjin			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620290" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>7-1 -&gt; 10-4 -&gt; 12-11 -&gt; 12-14 pls ban this fixers bots</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:36 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620290" data-author-name="sayjin">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620290">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620290/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="56">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620290"></div>
		<div class="reply-form" data-post-id="4620290"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4621241">
		<a id="154" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#154</div>
			
			<i class="post-header-flag flag mod-id" title="Indonesia"></i> 
			<a href="/user/Rairyuu" class="post-header-author  mod-vlr">
				Rairyuu			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621241" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Fix ur brain first 🤣</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:22 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621241" data-author-name="Rairyuu">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621241">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621241/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="154">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621241"></div>
		<div class="reply-form" data-post-id="4621241"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620292">
		<a id="57" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#57</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/Dhrom49" class="post-header-author  mod-vlr">
				Dhrom49			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/1034/nrg-esports"><img class="post-header-flair" src="//owcdn.net/img/6610f02d2d7b0.png" title="NRG Esports"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620292" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Less is more</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:36 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620292" data-author-name="Dhrom49">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620292">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620292/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="57">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620292"></div>
		<div class="reply-form" data-post-id="4620292"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620293">
		<a id="58" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#58</div>
			
			<i class="post-header-flag flag mod-id" title="Indonesia"></i> 
			<a href="/user/OWEN" class="post-header-author  mod-vlr">
				OWEN			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620293" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>10-4 to 12-14 cinema</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:36 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620293" data-author-name="OWEN">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620293">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620293/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="58">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620293"></div>
		<div class="reply-form" data-post-id="4620293"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4623534">
		<a id="177" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#177</div>
			
			<i class="post-header-flag flag mod-kr" title="South Korea"></i> 
			<a href="/user/KoreaVlr" class="post-header-author  mod-vlr">
				KoreaVlr			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4623534" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>But finally T1 won lol</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Mar 1, 2025 at 9:42 AM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4623534" data-author-name="KoreaVlr">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4623534">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4623534/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="177">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4623534"></div>
		<div class="reply-form" data-post-id="4623534"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620304">
		<a id="59" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#59</div>
			
			<i class="post-header-flag flag mod-ca" title="Canada"></i> 
			<a href="/user/keanejasper" class="post-header-author  mod-vlr">
				keanejasper			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/13565/3"><img class="post-header-flair" src="//owcdn.net/img/6519caa187408.png" title=":3"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620304" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-3 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>korean valorant never makes it higher than top 4</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:36 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620304" data-author-name="keanejasper">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620304">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620304/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="59">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620304"></div>
		<div class="reply-form" data-post-id="4620304"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620344">
		<a id="66" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#66</div>
			
			<i class="post-header-flag flag mod-kr" title="South Korea"></i> 
			<a href="/user/Daechudang_" class="post-header-author  mod-vlr">
				Daechudang_			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620344" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>:3</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:39 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620344" data-author-name="Daechudang_">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620344">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620344/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="66">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620344"></div>
		<div class="reply-form" data-post-id="4620344"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620363">
		<a id="71" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#71</div>
			
			<i class="post-header-flag flag mod-in" title="India"></i> 
			<a href="/user/Luffyo7" class="post-header-author  mod-vlr">
				Luffyo7			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620363" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Nah top 3 they can't achieve more than that</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:41 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620363" data-author-name="Luffyo7">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620363">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620363/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="71">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620363"></div>
		<div class="reply-form" data-post-id="4620363"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4620378">
		<a id="74" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#74</div>
			
			<i class="post-header-flag flag mod-vi" title="Virgin Islands, U.S."></i> 
			<a href="/user/Anzaldinho" class="post-header-author  mod-vlr">
				Anzaldinho			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620378" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>are you dementic</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:43 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620378" data-author-name="Anzaldinho">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620378">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620378/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="74">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620378"></div>
		<div class="reply-form" data-post-id="4620378"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620371">
		<a id="73" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#73</div>
			
			<i class="post-header-flag flag mod-vi" title="Virgin Islands, U.S."></i> 
			<a href="/user/Anzaldinho" class="post-header-author  mod-vlr">
				Anzaldinho			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620371" data-frag-status="neutral">
					<div class="post-frag-count positive">
						4 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>bro must have forgotten about the existence of gen g</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:42 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620371" data-author-name="Anzaldinho">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620371">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620371/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="73">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620371"></div>
		<div class="reply-form" data-post-id="4620371"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620305">
		<a id="60" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#60</div>
			
			<i class="post-header-flag flag mod-jp" title="Japan"></i> 
			<a href="/user/Diipsheet" class="post-header-author  mod-vlr">
				Diipsheet			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/7932/onlyfins"><img class="post-header-flair" src="//owcdn.net/img/669f7817868bf.png" title="OnlyFins"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620305" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Izu doing Flashback cosplay</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:36 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620305" data-author-name="Diipsheet">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620305">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620305/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="60">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620305"></div>
		<div class="reply-form" data-post-id="4620305"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620320">
		<a id="61" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#61</div>
			
			<i class="post-header-flag flag mod-lv" title="Latvia"></i> 
			<a href="/user/johnlenin" class="post-header-author  mod-vlr">
				johnlenin			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/8185/drx"><img class="post-header-flair" src="//owcdn.net/img/63b17ac3a7d00.png" title="DRX"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620320" data-frag-status="neutral">
					<div class="post-frag-count positive">
						4 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>T1 actors eating good 😋<br />
good game well paid 🤑</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:37 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620320" data-author-name="johnlenin">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620320">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620320/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="61">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620320"></div>
		<div class="reply-form" data-post-id="4620320"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620322">
		<a id="62" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#62</div>
			
			<i class="post-header-flag flag mod-eu" title="Europe"></i> 
			<a href="/user/kekW_gaming" class="post-header-author  mod-vlr">
				kekW_gaming			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620322" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>EZ APAC KEKW Gaming! Chokers! T1Chokers They forgot this is normal for comebacks for Derke</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:37 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620322" data-author-name="kekW_gaming">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620322">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620322/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="62">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620322"></div>
		<div class="reply-form" data-post-id="4620322"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4621103">
		<a id="144" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#144</div>
			
			<i class="post-header-flag flag mod-kr" title="South Korea"></i> 
			<a href="/user/zoro77ll" class="post-header-author  mod-vlr">
				zoro77ll			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/14/t1"><img class="post-header-flair" src="//owcdn.net/img/62fe0b8f6b084.png" title="T1"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621103" data-frag-status="neutral">
					<div class="post-frag-count positive">
						3 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>EZ EU</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:16 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621103" data-author-name="zoro77ll">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621103">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621103/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="144">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621103"></div>
		<div class="reply-form" data-post-id="4621103"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4622086">
		<a id="173" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#173</div>
			
			<i class="post-header-flag flag mod-id" title="Indonesia"></i> 
			<a href="/user/kev_94" class="post-header-author  mod-vlr">
				kev_94			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/14/t1"><img class="post-header-flair" src="//owcdn.net/img/62fe0b8f6b084.png" title="T1"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4622086" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Jerke</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 9:56 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4622086" data-author-name="kev_94">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4622086">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4622086/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="173">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4622086"></div>
		<div class="reply-form" data-post-id="4622086"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620332">
		<a id="63" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#63</div>
			
			<i class="post-header-flag flag mod-br" title="Brazil"></i> 
			<a href="/user/Miyuky" class="post-header-author  mod-vlr">
				Miyuky			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620332" data-frag-status="neutral">
					<div class="post-frag-count positive">
						2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Throwers1</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:38 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620332" data-author-name="Miyuky">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620332">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620332/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="63">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620332"></div>
		<div class="reply-form" data-post-id="4620332"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620349">
		<a id="67" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#67</div>
			
			<i class="post-header-flag flag mod-lv" title="Latvia"></i> 
			<a href="/user/Myhemcph" class="post-header-author  mod-vlr">
				Myhemcph			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620349" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>T sided map, u crying a lot about throws. Check another t1 and vita games on Lotus</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:40 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620349" data-author-name="Myhemcph">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620349">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620349/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="67">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620349"></div>
		<div class="reply-form" data-post-id="4620349"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620358">
		<a id="69" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#69</div>
			
			<i class="post-header-flag flag mod-in" title="India"></i> 
			<a href="/user/badger252" class="post-header-author  mod-vlr">
				badger252			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/120/100-thieves"><img class="post-header-flair" src="//owcdn.net/img/603c00dbb7d39.png" title="100 Thieves"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620358" data-frag-status="neutral">
					<div class="post-frag-count positive">
						3 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Yes in other match t1 threw from 9-5 as attackers on fracture(heavy t sided map)</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:41 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620358" data-author-name="badger252">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620358">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620358/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="69">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620358"></div>
		<div class="reply-form" data-post-id="4620358"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620366">
		<a id="72" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#72</div>
			
			<i class="post-header-flag flag mod-lv" title="Latvia"></i> 
			<a href="/user/johnlenin" class="post-header-author  mod-vlr">
				johnlenin			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/8185/drx"><img class="post-header-flair" src="//owcdn.net/img/63b17ac3a7d00.png" title="DRX"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620366" data-frag-status="neutral">
					<div class="post-frag-count positive">
						3 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>hello delusional latvian bro<br />
keep believing in fair cybersport in 2025 👍</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:42 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620366" data-author-name="johnlenin">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620366">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620366/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="72">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620366"></div>
		<div class="reply-form" data-post-id="4620366"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4620382">
		<a id="75" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#75</div>
			
			<i class="post-header-flag flag mod-in" title="India"></i> 
			<a href="/user/badger252" class="post-header-author  mod-vlr">
				badger252			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/120/100-thieves"><img class="post-header-flair" src="//owcdn.net/img/603c00dbb7d39.png" title="100 Thieves"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620382" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>dw bout him, just a WWE fan</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:43 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620382" data-author-name="badger252">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620382">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620382/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="75">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620382"></div>
		<div class="reply-form" data-post-id="4620382"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-3" data-post-id="4620423">
		<a id="77" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#77</div>
			
			<i class="post-header-flag flag mod-lv" title="Latvia"></i> 
			<a href="/user/johnlenin" class="post-header-author  mod-vlr">
				johnlenin			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/8185/drx"><img class="post-header-flair" src="//owcdn.net/img/63b17ac3a7d00.png" title="DRX"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620423" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Sadly most people are WWE fans</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:48 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620423" data-author-name="johnlenin">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620423">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620423/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="77">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620423"></div>
		<div class="reply-form" data-post-id="4620423"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-3" data-post-id="4620457">
		<a id="79" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#79</div>
			
			<i class="post-header-flag flag mod-lv" title="Latvia"></i> 
			<a href="/user/Myhemcph" class="post-header-author  mod-vlr">
				Myhemcph			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620457" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Better find 322 everywhere my gambling addict friend, then took ur losses.</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:54 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620457" data-author-name="Myhemcph">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620457">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620457/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="79">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620457"></div>
		<div class="reply-form" data-post-id="4620457"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4620480">
		<a id="83" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#83</div>
			
			<i class="post-header-flag flag mod-lv" title="Latvia"></i> 
			<a href="/user/Myhemcph" class="post-header-author  mod-vlr">
				Myhemcph			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620480" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Probably not, but if u keep believing that every tier 1 match on LAN hits matchfix, then what are doing here? Circus fits better w/o nerves and money usage. Better to believe that its fair play, cause even me with my friends often comeback from dead scores in mm, why shouldnt this happen here?  If u see matchfix everywhere and accept it, it proves u gift money to bookies, and should ashame urself, not teams</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:01 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620480" data-author-name="Myhemcph">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620480">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620480/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="83">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620480"></div>
		<div class="reply-form" data-post-id="4620480"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620427">
		<a id="78" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#78</div>
			
			<i class="post-header-flag flag mod-cn" title="China"></i> 
			<a href="/user/withsn" class="post-header-author  mod-vlr">
				withsn			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620427" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>for kr team lotus are a balance map, maybe even a little ct sided. considering its a close game only the clutch vitality wins makes the difference.</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:48 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620427" data-author-name="withsn">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620427">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620427/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="78">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620427"></div>
		<div class="reply-form" data-post-id="4620427"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620465">
		<a id="80" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#80</div>
			
			<i class="post-header-flag flag mod-br" title="Brazil"></i> 
			<a href="/user/Amadeus11" class="post-header-author  mod-vlr">
				Amadeus11			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620465" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>map pick = LOSE lol</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:55 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620465" data-author-name="Amadeus11">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620465">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620465/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="80">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620465"></div>
		<div class="reply-form" data-post-id="4620465"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620476">
		<a id="81" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#81</div>
			
			<i class="post-header-flag flag mod-jp" title="Japan"></i> 
			<a href="/user/LULE" class="post-header-author  mod-vlr">
				LULE			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/4915/natus-vincere"><img class="post-header-flair" src="//owcdn.net/img/62a410a4e7b4f.png" title="Natus Vincere"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620476" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>they pulled out Sayf jett😭</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:57 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620476" data-author-name="LULE">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620476">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620476/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="81">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620476"></div>
		<div class="reply-form" data-post-id="4620476"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620525">
		<a id="86" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#86</div>
			
			<i class="post-header-flag flag mod-in" title="India"></i> 
			<a href="/user/TaniBoy7" class="post-header-author  mod-vlr">
				TaniBoy7			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/2/sentinels"><img class="post-header-flair" src="//owcdn.net/img/62875027c8e06.png" title="Sentinels"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620525" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>He's actually cooking ngl</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:14 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620525" data-author-name="TaniBoy7">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620525">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620525/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="86">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620525"></div>
		<div class="reply-form" data-post-id="4620525"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4620664">
		<a id="102" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#102</div>
			
			<i class="post-header-flag flag mod-jp" title="Japan"></i> 
			<a href="/user/LULE" class="post-header-author  mod-vlr">
				LULE			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/4915/natus-vincere"><img class="post-header-flair" src="//owcdn.net/img/62a410a4e7b4f.png" title="Natus Vincere"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620664" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>nah I mean like why does HE have to play JETT?? why not support Derke on tejo or be a secondary entry on Iso? his Iso looked way better</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:32 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620664" data-author-name="LULE">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620664">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620664/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="102">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620664"></div>
		<div class="reply-form" data-post-id="4620664"></div>
	</div>
</div></div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620477">
		<a id="82" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#82</div>
			
			<i class="post-header-flag flag mod-sg" title="Singapore"></i> 
			<a href="/user/Araceae" class="post-header-author  mod-vlr">
				Araceae			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620477" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>fk botality shitshow</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 6:58 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620477" data-author-name="Araceae">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620477">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620477/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="82">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620477"></div>
		<div class="reply-form" data-post-id="4620477"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620514">
		<a id="84" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#84</div>
			
			<i class="post-header-flag flag mod-kr" title="South Korea"></i> 
			<a href="/user/grenade" class="post-header-author  mod-vlr">
				grenade			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620514" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-6 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>trash1 looks so bad go home buddy</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:11 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620514" data-author-name="grenade">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620514">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620514/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="84">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620514"></div>
		<div class="reply-form" data-post-id="4620514"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4623795">
		<a id="178" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#178</div>
			
			<i class="post-header-flag flag mod-vn" title="Vietnam"></i> 
			<a href="/user/yungzico" class="post-header-author  mod-vlr">
				yungzico			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/624/paper-rex"><img class="post-header-flair" src="//owcdn.net/img/62bbebb185a7e.png" title="Paper Rex"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4623795" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>exit match, enter airport XDDDD</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Mar 1, 2025 at 12:56 PM IST">
					 1 day ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4623795" data-author-name="yungzico">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4623795">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4623795/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="178">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4623795"></div>
		<div class="reply-form" data-post-id="4623795"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620522">
		<a id="85" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#85</div>
			
			<i class="post-header-flag flag mod-dk" title="Denmark"></i> 
			<a href="/user/trola" class="post-header-author  mod-vlr">
				trola			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/474/team-liquid"><img class="post-header-flair" src="//owcdn.net/img/640c38262824c.png" title="Team Liquid"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620522" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>wtf was happening how did t1 throw that 1st map lol</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:14 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620522" data-author-name="trola">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620522">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620522/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="85">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620522"></div>
		<div class="reply-form" data-post-id="4620522"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620528">
		<a id="87" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#87</div>
			
			<i class="post-header-flag flag mod-hk" title="Hong Kong"></i> 
			<a href="/user/milkywayyyyy" class="post-header-author  mod-vlr">
				milkywayyyyy			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620528" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>classic map pick trade , feel like watching wwe</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:16 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620528" data-author-name="milkywayyyyy">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620528">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620528/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="87">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620528"></div>
		<div class="reply-form" data-post-id="4620528"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620531">
		<a id="88" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#88</div>
			
			<i class="post-header-flag flag mod-br" title="Brazil"></i> 
			<a href="/user/arthuraousurta" class="post-header-author  mod-vlr">
				arthuraousurta			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620531" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>vit trash asf, cant play own map pick, so dumb rounds lost like silver bots</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:16 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620531" data-author-name="arthuraousurta">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620531">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620531/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="88">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620531"></div>
		<div class="reply-form" data-post-id="4620531"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620562">
		<a id="89" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#89</div>
			
			<i class="post-header-flag flag mod-ru" title="Russia"></i> 
			<a href="/user/Syr0m" class="post-header-author  mod-vlr">
				Syr0m			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/2059/team-vitality"><img class="post-header-flair" src="//owcdn.net/img/6466d7936fd86.png" title="Team Vitality"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620562" data-frag-status="neutral">
					<div class="post-frag-count positive">
						2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>stop gambling and get a job </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:21 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620562" data-author-name="Syr0m">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620562">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620562/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="89">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620562"></div>
		<div class="reply-form" data-post-id="4620562"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4620582">
		<a id="93" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#93</div>
			
			<i class="post-header-flag flag mod-br" title="Brazil"></i> 
			<a href="/user/arthuraousurta" class="post-header-author  mod-vlr">
				arthuraousurta			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620582" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>cant have a job and also gambling?</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:23 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620582" data-author-name="arthuraousurta">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620582">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620582/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="93">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620582"></div>
		<div class="reply-form" data-post-id="4620582"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-3" data-post-id="4620622">
		<a id="98" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#98</div>
			
			<i class="post-header-flag flag mod-ru" title="Russia"></i> 
			<a href="/user/Syr0m" class="post-header-author  mod-vlr">
				Syr0m			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/2059/team-vitality"><img class="post-header-flair" src="//owcdn.net/img/6466d7936fd86.png" title="Team Vitality"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620622" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>that is even worse 💀</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:27 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620622" data-author-name="Syr0m">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620622">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620622/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="98">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620622"></div>
		<div class="reply-form" data-post-id="4620622"></div>
	</div>
</div></div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620626">
		<a id="99" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#99</div>
			
			<i class="post-header-flag flag mod-cn" title="China"></i> 
			<a href="/user/withsn" class="post-header-author  mod-vlr">
				withsn			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620626" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>same things happens a lot on fps game, and since they played the classic map so they cant out play each other on map strategy, both of two team can  play these map.</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:27 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620626" data-author-name="withsn">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620626">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620626/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="99">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620626"></div>
		<div class="reply-form" data-post-id="4620626"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620567">
		<a id="90" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#90</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/100Tchoke" class="post-header-author  mod-vlr">
				100Tchoke			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620567" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>NICEUUU. T1 is winning. VIT are horrible after map 2</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:22 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620567" data-author-name="100Tchoke">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620567">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620567/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="90">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620567"></div>
		<div class="reply-form" data-post-id="4620567"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620578">
		<a id="91" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#91</div>
			
			<i class="post-header-flag flag mod-pl" title="Poland"></i> 
			<a href="/user/Apaqt" class="post-header-author  mod-vlr">
				Apaqt			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620578" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>3-12 Less💀</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:23 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620578" data-author-name="Apaqt">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620578">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620578/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="91">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620578"></div>
		<div class="reply-form" data-post-id="4620578"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620580">
		<a id="92" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#92</div>
			
			<i class="post-header-flag flag mod-ru" title="Russia"></i> 
			<a href="/user/brezyyy" class="post-header-author  mod-vlr">
				brezyyy			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620580" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>and again VIT extremely lucky to even have a chance for split<br />
Less bailed them out on lotus, and 2v1 on 10-4 as well</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:23 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620580" data-author-name="brezyyy">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620580">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620580/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="92">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620580"></div>
		<div class="reply-form" data-post-id="4620580"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620593">
		<a id="94" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#94</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/yehfela" class="post-header-author  mod-vlr">
				yehfela			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/11060/nongshim-redforce"><img class="post-header-flair" src="//owcdn.net/img/6399bb707aacb.png" title="Nongshim RedForce"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620593" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Less?</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:24 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620593" data-author-name="yehfela">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620593">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620593/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="94">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620593"></div>
		<div class="reply-form" data-post-id="4620593"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620596">
		<a id="95" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#95</div>
			
			<i class="post-header-flag flag mod-jp" title="Japan"></i> 
			<a href="/user/ShibaIZu" class="post-header-author  mod-vlr">
				ShibaIZu			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620596" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Every asian know western have better luck the asian</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:24 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620596" data-author-name="ShibaIZu">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620596">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620596/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="95">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620596"></div>
		<div class="reply-form" data-post-id="4620596"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620615">
		<a id="96" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#96</div>
			
			<i class="post-header-flag flag mod-eu" title="Europe"></i> 
			<a href="/user/kekW_gaming" class="post-header-author  mod-vlr">
				kekW_gaming			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620615" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>WTF was that from Botality. Imagine if they lost Map 1 and still went with that Comp. Kekw Don't fix what is not broken. What an anticlimactic game of Buzz vs Derke on Yoru. A certified disasterclass KEKW Gaming from them </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:26 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620615" data-author-name="kekW_gaming">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620615">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620615/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="96">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620615"></div>
		<div class="reply-form" data-post-id="4620615"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620621">
		<a id="97" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#97</div>
			
			<i class="post-header-flag flag mod-au" title="Australia"></i> 
			<a href="/user/Lzke" class="post-header-author  mod-vlr">
				Lzke			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620621" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>I feel like Less is underperforming severely, even yesterday xD</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:27 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620621" data-author-name="Lzke">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620621">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620621/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="97">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620621"></div>
		<div class="reply-form" data-post-id="4620621"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620633">
		<a id="100" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#100</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/Bot_teams" class="post-header-author  mod-vlr">
				Bot_teams			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620633" data-frag-status="neutral">
					<div class="post-frag-count positive">
						2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>2-1 T1</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:27 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620633" data-author-name="Bot_teams">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620633">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620633/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="100">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620633"></div>
		<div class="reply-form" data-post-id="4620633"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620641">
		<a id="101" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#101</div>
			
			<i class="post-header-flag flag mod-ba" title="Bosnia and Herzegovina"></i> 
			<a href="/user/sergueiessenine" class="post-header-author  mod-vlr">
				sergueiessenine			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/8185/drx"><img class="post-header-flair" src="//owcdn.net/img/63b17ac3a7d00.png" title="DRX"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620641" data-frag-status="neutral">
					<div class="post-frag-count positive">
						4 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>free trexx</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:29 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620641" data-author-name="sergueiessenine">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620641">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620641/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="101">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620641"></div>
		<div class="reply-form" data-post-id="4620641"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620699">
		<a id="103" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#103</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/Bot_teams" class="post-header-author  mod-vlr">
				Bot_teams			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620699" data-frag-status="neutral">
					<div class="post-frag-count positive">
						2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Thrifty ez t1 map 3 game over</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:39 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620699" data-author-name="Bot_teams">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620699">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620699/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="103">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620699"></div>
		<div class="reply-form" data-post-id="4620699"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620706">
		<a id="105" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#105</div>
			
			<i class="post-header-flag flag mod-hk" title="Hong Kong"></i> 
			<a href="/user/milkywayyyyy" class="post-header-author  mod-vlr">
				milkywayyyyy			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620706" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>what this botality doing lol</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:40 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620706" data-author-name="milkywayyyyy">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620706">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620706/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="105">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620706"></div>
		<div class="reply-form" data-post-id="4620706"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620721">
		<a id="106" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#106</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/Bot_teams" class="post-header-author  mod-vlr">
				Bot_teams			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620721" data-frag-status="neutral">
					<div class="post-frag-count positive">
						3 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>T1 stronger team lol </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:42 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620721" data-author-name="Bot_teams">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620721">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620721/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="106">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620721"></div>
		<div class="reply-form" data-post-id="4620721"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620723">
		<a id="107" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#107</div>
			
			<i class="post-header-flag flag mod-ru" title="Russia"></i> 
			<a href="/user/brezyyy" class="post-header-author  mod-vlr">
				brezyyy			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620723" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Korea I beg stop 3v2 peeking </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:43 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620723" data-author-name="brezyyy">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620723">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620723/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="107">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620723"></div>
		<div class="reply-form" data-post-id="4620723"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620729">
		<a id="108" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#108</div>
			
			<i class="post-header-flag flag mod-au" title="Australia"></i> 
			<a href="/user/Lzke" class="post-header-author  mod-vlr">
				Lzke			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620729" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>4v2. GG Vit win, no discipline. </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:43 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620729" data-author-name="Lzke">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620729">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620729/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="108">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620729"></div>
		<div class="reply-form" data-post-id="4620729"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620734">
		<a id="109" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#109</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/Bot_teams" class="post-header-author  mod-vlr">
				Bot_teams			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620734" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>No way botality take this lmao</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:44 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620734" data-author-name="Bot_teams">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620734">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620734/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="109">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620734"></div>
		<div class="reply-form" data-post-id="4620734"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620754">
		<a id="110" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#110</div>
			
			<i class="post-header-flag flag mod-al" title="Albania"></i> 
			<a href="/user/Vlrdodmog" class="post-header-author  mod-vlr">
				Vlrdodmog			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620754" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Those guys really need to thank the lord for blessing them to be working in eu cuz no way some of them should be getting paid 6 digit per year</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:49 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620754" data-author-name="Vlrdodmog">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620754">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620754/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="110">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620754"></div>
		<div class="reply-form" data-post-id="4620754"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620781">
		<a id="111" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#111</div>
			
			<i class="post-header-flag flag mod-ru" title="Russia"></i> 
			<a href="/user/brezyyy" class="post-header-author  mod-vlr">
				brezyyy			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620781" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>there are actually many pros who make abysmal mistakes while getting paid a lot </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:53 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620781" data-author-name="brezyyy">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620781">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620781/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="111">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620781"></div>
		<div class="reply-form" data-post-id="4620781"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620784">
		<a id="112" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#112</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/Bot_teams" class="post-header-author  mod-vlr">
				Bot_teams			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620784" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Pure korean team too strong </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:53 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620784" data-author-name="Bot_teams">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620784">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620784/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="112">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620784"></div>
		<div class="reply-form" data-post-id="4620784"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620811">
		<a id="113" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#113</div>
			
			<i class="post-header-flag flag mod-kp" title="North Korea"></i> 
			<a href="/user/Eoghan4" class="post-header-author  mod-vlr">
				Eoghan4			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/12694/gentle-mates"><img class="post-header-flair" src="//owcdn.net/img/66701546055dd.png" title="Gentle Mates"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620811" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>bruh</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:56 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620811" data-author-name="Eoghan4">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620811">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620811/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="113">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620811"></div>
		<div class="reply-form" data-post-id="4620811"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620819">
		<a id="114" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#114</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/Bot_teams" class="post-header-author  mod-vlr">
				Bot_teams			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620819" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Too easy guys too easy</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:57 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620819" data-author-name="Bot_teams">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620819">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620819/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="114">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620819"></div>
		<div class="reply-form" data-post-id="4620819"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620821">
		<a id="115" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#115</div>
			
			<i class="post-header-flag flag mod-br" title="Brazil"></i> 
			<a href="/user/Amadeus11" class="post-header-author  mod-vlr">
				Amadeus11			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620821" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>again win pistol and lose the next rounds. VIT = pure trash</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:57 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620821" data-author-name="Amadeus11">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620821">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620821/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="115">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620821"></div>
		<div class="reply-form" data-post-id="4620821"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620828">
		<a id="116" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#116</div>
			
			<i class="post-header-flag flag mod-bn" title="Brunei Darussalam"></i> 
			<a href="/user/nacelnik" class="post-header-author  mod-vlr">
				nacelnik			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620828" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>How they win map 1</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 7:57 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620828" data-author-name="nacelnik">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620828">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620828/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="116">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620828"></div>
		<div class="reply-form" data-post-id="4620828"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620863">
		<a id="118" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#118</div>
			
			<i class="post-header-flag flag mod-br" title="Brazil"></i> 
			<a href="/user/DrSiemann" class="post-header-author  mod-vlr">
				DrSiemann			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620863" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>wtf happened to Vitality</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:01 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620863" data-author-name="DrSiemann">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620863">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620863/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="118">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620863"></div>
		<div class="reply-form" data-post-id="4620863"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620901">
		<a id="120" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#120</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/Bot_teams" class="post-header-author  mod-vlr">
				Bot_teams			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620901" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>What you guys expecting on weaker team?</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:03 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620901" data-author-name="Bot_teams">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620901">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620901/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="120">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620901"></div>
		<div class="reply-form" data-post-id="4620901"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4621660">
		<a id="169" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#169</div>
			
			<i class="post-header-flag flag mod-br" title="Brazil"></i> 
			<a href="/user/DrSiemann" class="post-header-author  mod-vlr">
				DrSiemann			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621660" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>vit is 3x2 against T1 in maps this tournament, but okay.</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:50 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621660" data-author-name="DrSiemann">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621660">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621660/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="169">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621660"></div>
		<div class="reply-form" data-post-id="4621660"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-3" data-post-id="4623871">
		<a id="181" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#181</div>
			
			<i class="post-header-flag flag mod-kr" title="South Korea"></i> 
			<a href="/user/Dreoxx" class="post-header-author  mod-vlr">
				Dreoxx			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/8185/drx"><img class="post-header-flair" src="//owcdn.net/img/63b17ac3a7d00.png" title="DRX"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4623871" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>and T1 is 57-49 on rounds, but okay. shows how throw1 just manages to lose maps while being the better team</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Mar 1, 2025 at 2:08 PM IST">
					 1 day ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4623871" data-author-name="Dreoxx">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4623871">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4623871/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="181">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4623871"></div>
		<div class="reply-form" data-post-id="4623871"></div>
	</div>
</div></div></div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620898">
		<a id="119" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#119</div>
			
			<i class="post-header-flag flag mod-gb" title="United Kingdom"></i> 
			<a href="/user/sugaclutch" class="post-header-author  mod-vlr">
				sugaclutch			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620898" data-frag-status="neutral">
					<div class="post-frag-count positive">
						2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>th wouldn't let it slide btw..botality</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:03 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620898" data-author-name="sugaclutch">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620898">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620898/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="119">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620898"></div>
		<div class="reply-form" data-post-id="4620898"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620902">
		<a id="121" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#121</div>
			
			<i class="post-header-flag flag mod-in" title="India"></i> 
			<a href="/user/badger252" class="post-header-author  mod-vlr">
				badger252			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/120/100-thieves"><img class="post-header-flair" src="//owcdn.net/img/603c00dbb7d39.png" title="100 Thieves"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620902" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>all that comeback bs 1st map for this lmao<br />
vitality = 🤡🤡</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:03 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620902" data-author-name="badger252">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620902">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620902/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="121">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620902"></div>
		<div class="reply-form" data-post-id="4620902"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620903">
		<a id="122" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#122</div>
			
			<i class="post-header-flag flag mod-un" title="International"></i> 
			<a href="/user/vyltx" class="post-header-author  mod-vlr">
				vyltx			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/6961/loud"><img class="post-header-flair" src="//owcdn.net/img/62bbec8dc1b9f.png" title="LOUD"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620903" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>how is this superteam losing😭😭✌️✌️</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:03 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620903" data-author-name="vyltx">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620903">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620903/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="122">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620903"></div>
		<div class="reply-form" data-post-id="4620903"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620918">
		<a id="124" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#124</div>
			
			<i class="post-header-flag flag mod-pl" title="Poland"></i> 
			<a href="/user/tong5" class="post-header-author  mod-vlr">
				tong5			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/474/team-liquid"><img class="post-header-flair" src="//owcdn.net/img/640c38262824c.png" title="Team Liquid"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620918" data-frag-status="neutral">
					<div class="post-frag-count positive">
						5 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Imagine calling these 4 randoms + Derke a superteam XD </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:05 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620918" data-author-name="tong5">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620918">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620918/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="124">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620918"></div>
		<div class="reply-form" data-post-id="4620918"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4621401">
		<a id="162" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#162</div>
			
			<i class="post-header-flag flag mod-br" title="Brazil"></i> 
			<a href="/user/zarpela" class="post-header-author  mod-vlr">
				zarpela			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/6961/loud"><img class="post-header-flair" src="//owcdn.net/img/62bbec8dc1b9f.png" title="LOUD"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621401" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>flair</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:29 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621401" data-author-name="zarpela">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621401">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621401/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="162">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621401"></div>
		<div class="reply-form" data-post-id="4621401"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4626044">
		<a id="182" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#182</div>
			
			<i class="post-header-flag flag mod-so" title="Somalia"></i> 
			<a href="/user/SudokuDude" class="post-header-author  mod-vlr">
				SudokuDude			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4626044" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Less isn't a random. 😂😂😂</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Mar 1, 2025 at 9:50 PM IST">
					 1 day ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4626044" data-author-name="SudokuDude">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4626044">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4626044/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="182">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4626044"></div>
		<div class="reply-form" data-post-id="4626044"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620969">
		<a id="128" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#128</div>
			
			<i class="post-header-flag flag mod-un" title="International"></i> 
			<a href="/user/Prathades" class="post-header-author  mod-vlr">
				Prathades			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/878/rex-regum-qeon"><img class="post-header-flair" src="//owcdn.net/img/629f17f51e7a3.png" title="Rex Regum Qeon"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620969" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>A superteam of a shit region is still shit. </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:12 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620969" data-author-name="Prathades">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620969">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620969/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="128">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620969"></div>
		<div class="reply-form" data-post-id="4620969"></div>
	</div>
</div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620914">
		<a id="123" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#123</div>
			
			<i class="post-header-flag flag mod-gb" title="United Kingdom"></i> 
			<a href="/user/maxverstappen" class="post-header-author  mod-vlr">
				maxverstappen			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620914" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Bye  vitality.  Super team they said 🤡🤡🤡</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:05 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620914" data-author-name="maxverstappen">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620914">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620914/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="123">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620914"></div>
		<div class="reply-form" data-post-id="4620914"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620957">
		<a id="125" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#125</div>
			
			<i class="post-header-flag flag mod-gb" title="United Kingdom"></i> 
			<a href="/user/sugaclutch" class="post-header-author  mod-vlr">
				sugaclutch			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620957" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>superteam doing the sloppy set plays???? ewwwww </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:10 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620957" data-author-name="sugaclutch">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620957">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620957/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="125">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620957"></div>
		<div class="reply-form" data-post-id="4620957"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620959">
		<a id="126" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#126</div>
			
			<i class="post-header-flag flag mod-us" title="United States"></i> 
			<a href="/user/Bot_teams" class="post-header-author  mod-vlr">
				Bot_teams			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620959" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>😂</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:10 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620959" data-author-name="Bot_teams">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620959">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620959/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="126">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620959"></div>
		<div class="reply-form" data-post-id="4620959"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620966">
		<a id="127" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#127</div>
			
			<i class="post-header-flag flag mod-gb" title="United Kingdom"></i> 
			<a href="/user/opalesnt" class="post-header-author  mod-vlr">
				opalesnt			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/8304/talon"><img class="post-header-flair" src="//owcdn.net/img/6226f3d764e03.png" title="TALON"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620966" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>T1 MY GOATS</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:11 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620966" data-author-name="opalesnt">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620966">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620966/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="127">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620966"></div>
		<div class="reply-form" data-post-id="4620966"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4620972">
		<a id="129" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#129</div>
			
			<i class="post-header-flag flag mod-ru" title="Russia"></i> 
			<a href="/user/brezyyy" class="post-header-author  mod-vlr">
				brezyyy			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620972" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>finally fluke 6 win streak run is over and heavily star play team is down</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:12 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620972" data-author-name="brezyyy">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620972">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620972/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="129">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620972"></div>
		<div class="reply-form" data-post-id="4620972"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-1" data-post-id="4620999">
		<a id="130" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#130</div>
			
			<i class="post-header-flag flag mod-gb" title="United Kingdom"></i> 
			<a href="/user/sugaclutch" class="post-header-author  mod-vlr">
				sugaclutch			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4620999" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>there is no star player except derke and less...they are both kinna washed too...sayf igling is fuckin trash</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:13 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4620999" data-author-name="sugaclutch">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4620999">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4620999/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="130">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4620999"></div>
		<div class="reply-form" data-post-id="4620999"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-2" data-post-id="4621032">
		<a id="132" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#132</div>
			
			<i class="post-header-flag flag mod-ru" title="Russia"></i> 
			<a href="/user/brezyyy" class="post-header-author  mod-vlr">
				brezyyy			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621032" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>ye you might be right, but still VIT heavily rely on individuals and suck as a team<br />
that's why Im hatin </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:15 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621032" data-author-name="brezyyy">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621032">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621032/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="132">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621032"></div>
		<div class="reply-form" data-post-id="4621032"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-3" data-post-id="4621137">
		<a id="148" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#148</div>
			
			<i class="post-header-flag flag mod-gb" title="United Kingdom"></i> 
			<a href="/user/sugaclutch" class="post-header-author  mod-vlr">
				sugaclutch			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/1001/team-heretics"><img class="post-header-flair" src="//owcdn.net/img/637b7557a9225.png" title="Team Heretics"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621137" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>bro don't speak truth...botality fans wont understand the concept of team chemistry that once had in '21 gambit, '23 fnc and '24 th...vibe and chemistry&gt;&gt;&gt;...something u cant buy with money</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:17 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621137" data-author-name="sugaclutch">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621137">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621137/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="148">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621137"></div>
		<div class="reply-form" data-post-id="4621137"></div>
	</div>
</div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-4" data-post-id="4621207">
		<a id="153" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#153</div>
			
			<i class="post-header-flag flag mod-ru" title="Russia"></i> 
			<a href="/user/brezyyy" class="post-header-author  mod-vlr">
				brezyyy			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621207" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>true true, good examples<br />
I miss Gambit :(</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:20 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621207" data-author-name="brezyyy">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621207">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621207/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="153">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621207"></div>
		<div class="reply-form" data-post-id="4621207"></div>
	</div>
</div></div></div></div></div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621022">
		<a id="131" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#131</div>
			
			<i class="post-header-flag flag mod-in" title="India"></i> 
			<a href="/user/badger252" class="post-header-author  mod-vlr">
				badger252			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/120/100-thieves"><img class="post-header-flair" src="//owcdn.net/img/603c00dbb7d39.png" title="100 Thieves"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621022" data-frag-status="neutral">
					<div class="post-frag-count positive">
						3 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Super Team ❌<br />
Super frauds ✅</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:14 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621022" data-author-name="badger252">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621022">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621022/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="131">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621022"></div>
		<div class="reply-form" data-post-id="4621022"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621039">
		<a id="133" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#133</div>
			
			<i class="post-header-flag flag mod-ba" title="Bosnia and Herzegovina"></i> 
			<a href="/user/sergueiessenine" class="post-header-author  mod-vlr">
				sergueiessenine			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/8185/drx"><img class="post-header-flair" src="//owcdn.net/img/63b17ac3a7d00.png" title="DRX"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621039" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>-sayf +nats<br />
-kicks +keiko<br />
-faded +bonkar </p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:15 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621039" data-author-name="sergueiessenine">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621039">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621039/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="133">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621039"></div>
		<div class="reply-form" data-post-id="4621039"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621040">
		<a id="134" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#134</div>
			
			<i class="post-header-flag flag mod-al" title="Albania"></i> 
			<a href="/user/Vlrdodmog" class="post-header-author  mod-vlr">
				Vlrdodmog			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621040" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>More flags than rounds win is insane guys wp</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:15 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621040" data-author-name="Vlrdodmog">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621040">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621040/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="134">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621040"></div>
		<div class="reply-form" data-post-id="4621040"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621044">
		<a id="135" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#135</div>
			
			<i class="post-header-flag flag mod-in" title="India"></i> 
			<a href="/user/9zze" class="post-header-author  mod-vlr">
				9zze			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/14/t1"><img class="post-header-flair" src="//owcdn.net/img/62fe0b8f6b084.png" title="T1"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621044" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Never had a doubt. Vct 2025 T1</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:15 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621044" data-author-name="9zze">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621044">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621044/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="135">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621044"></div>
		<div class="reply-form" data-post-id="4621044"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621048">
		<a id="136" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#136</div>
			
			<i class="post-header-flag flag mod-se" title="Sweden"></i> 
			<a href="/user/kAED" class="post-header-author  mod-vlr">
				kAED			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/14/t1"><img class="post-header-flair" src="//owcdn.net/img/62fe0b8f6b084.png" title="T1"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621048" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>The Silver 3 analyst desk and casters ONCE AGAIN overrating NA and EMEA teams.</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:15 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621048" data-author-name="kAED">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621048">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621048/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="136">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621048"></div>
		<div class="reply-form" data-post-id="4621048"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621064">
		<a id="139" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#139</div>
			
			<i class="post-header-flag flag mod-sg" title="Singapore"></i> 
			<a href="/user/Chok_Zense" class="post-header-author  mod-vlr">
				Chok_Zense			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/2/sentinels"><img class="post-header-flair" src="//owcdn.net/img/62875027c8e06.png" title="Sentinels"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621064" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>EMEA first seed kekw. So ass</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:15 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621064" data-author-name="Chok_Zense">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621064">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621064/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="139">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621064"></div>
		<div class="reply-form" data-post-id="4621064"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621067">
		<a id="140" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#140</div>
			
			<i class="post-header-flag flag mod-id" title="Indonesia"></i> 
			<a href="/user/MANIAC8686" class="post-header-author  mod-vlr">
				MANIAC8686			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/474/team-liquid"><img class="post-header-flair" src="//owcdn.net/img/640c38262824c.png" title="Team Liquid"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621067" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Extinction of trexx</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:15 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621067" data-author-name="MANIAC8686">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621067">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621067/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="140">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621067"></div>
		<div class="reply-form" data-post-id="4621067"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621079">
		<a id="141" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#141</div>
			
			<i class="post-header-flag flag mod-lv" title="Latvia"></i> 
			<a href="/user/johnlenin" class="post-header-author  mod-vlr">
				johnlenin			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-2"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/8185/drx"><img class="post-header-flair" src="//owcdn.net/img/63b17ac3a7d00.png" title="DRX"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621079" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-4 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>beautiful matchfixing from both teams 🤑</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:16 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621079" data-author-name="johnlenin">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621079">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621079/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="141">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621079"></div>
		<div class="reply-form" data-post-id="4621079"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621088">
		<a id="142" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#142</div>
			
			<i class="post-header-flag flag mod-dk" title="Denmark"></i> 
			<a href="/user/trola" class="post-header-author  mod-vlr">
				trola			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/474/team-liquid"><img class="post-header-flair" src="//owcdn.net/img/640c38262824c.png" title="Team Liquid"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621088" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>It's sad to EMEA's state right now. Other regions are developing but they are declining</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:16 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621088" data-author-name="trola">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621088">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621088/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="142">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621088"></div>
		<div class="reply-form" data-post-id="4621088"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621093">
		<a id="143" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#143</div>
			
			<i class="post-header-flag flag mod-gb" title="United Kingdom"></i> 
			<a href="/user/opalesnt" class="post-header-author  mod-vlr">
				opalesnt			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/8304/talon"><img class="post-header-flair" src="//owcdn.net/img/6226f3d764e03.png" title="TALON"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621093" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>3-0</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:16 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621093" data-author-name="opalesnt">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621093">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621093/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="143">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621093"></div>
		<div class="reply-form" data-post-id="4621093"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621104">
		<a id="145" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#145</div>
			
			<i class="post-header-flag flag mod-ph" title="Philippines"></i> 
			<a href="/user/Axauleon" class="post-header-author  mod-vlr">
				Axauleon			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/624/paper-rex"><img class="post-header-flair" src="//owcdn.net/img/62bbebb185a7e.png" title="Paper Rex"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621104" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>D0rke</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:17 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621104" data-author-name="Axauleon">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621104">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621104/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="145">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621104"></div>
		<div class="reply-form" data-post-id="4621104"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621130">
		<a id="146" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#146</div>
			
			<i class="post-header-flag flag mod-nl" title="Netherlands"></i> 
			<a href="/user/bahd0" class="post-header-author  mod-vlr">
				bahd0			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/11058/g2-esports"><img class="post-header-flair" src="//owcdn.net/img/633822848a741.png" title="G2 Esports"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621130" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Buzz you rocked mu chungus fuck life</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:17 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621130" data-author-name="bahd0">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621130">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621130/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="146">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621130"></div>
		<div class="reply-form" data-post-id="4621130"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621131">
		<a id="147" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#147</div>
			
			<i class="post-header-flag flag mod-kr" title="South Korea"></i> 
			<a href="/user/Seo_w" class="post-header-author  mod-vlr">
				Seo_w			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/11348/dplus-esports"><img class="post-header-flair" src="//owcdn.net/img/63bbe509420d5.png" title="Dplus Esports"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621131" data-frag-status="neutral">
					<div class="post-frag-count positive">
						2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>great bounce back from painful comeback, everyone looks really good and can cover each other, wp gg!</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:17 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621131" data-author-name="Seo_w">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621131">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621131/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="147">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621131"></div>
		<div class="reply-form" data-post-id="4621131"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621150">
		<a id="150" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#150</div>
			
			<i class="post-header-flag flag mod-id" title="Indonesia"></i> 
			<a href="/user/MANIAC8686" class="post-header-author  mod-vlr">
				MANIAC8686			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/474/team-liquid"><img class="post-header-flair" src="//owcdn.net/img/640c38262824c.png" title="Team Liquid"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621150" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Let's go T1</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:18 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621150" data-author-name="MANIAC8686">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621150">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621150/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="150">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621150"></div>
		<div class="reply-form" data-post-id="4621150"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621180">
		<a id="151" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#151</div>
			
			<i class="post-header-flag flag mod-jp" title="Japan"></i> 
			<a href="/user/LULE" class="post-header-author  mod-vlr">
				LULE			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/4915/natus-vincere"><img class="post-header-flair" src="//owcdn.net/img/62a410a4e7b4f.png" title="Natus Vincere"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621180" data-frag-status="neutral">
					<div class="post-frag-count positive">
						1 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>T1 played much better today. Buzz fragged the shit out of them.</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:19 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621180" data-author-name="LULE">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621180">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621180/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="151">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621180"></div>
		<div class="reply-form" data-post-id="4621180"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621191">
		<a id="152" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#152</div>
			
			<i class="post-header-flag flag mod-un" title="International"></i> 
			<a href="/user/Wotah" class="post-header-author  mod-vlr">
				Wotah			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621191" data-frag-status="neutral">
					<div class="post-frag-count positive">
						12 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Buzz became what everyone feared. His eyelids disappeared, his head was swelling and his ears started bleeding. &quot;Are you okay Buzz&quot; asks Meteor. I've never been better Meteor, I see it all now, they're not going A or B. They're going home.</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:20 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621191" data-author-name="Wotah">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621191">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621191/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="152">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621191"></div>
		<div class="reply-form" data-post-id="4621191"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621242">
		<a id="155" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#155</div>
			
			<i class="post-header-flag flag mod-in" title="India"></i> 
			<a href="/user/avenger50000" class="post-header-author  mod-vlr">
				avenger50000			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/14/t1"><img class="post-header-flair" src="//owcdn.net/img/62fe0b8f6b084.png" title="T1"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621242" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Sweet revenge on Vitality. Edward's next!!!</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:22 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621242" data-author-name="avenger50000">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621242">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621242/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="155">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621242"></div>
		<div class="reply-form" data-post-id="4621242"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621249">
		<a id="156" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#156</div>
			
			<i class="post-header-flag flag mod-un" title="International"></i> 
			<a href="/user/Bl1th" class="post-header-author  mod-vlr">
				Bl1th			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/11060/nongshim-redforce"><img class="post-header-flair" src="//owcdn.net/img/6399bb707aacb.png" title="Nongshim RedForce"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621249" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>BOTALITY</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:22 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621249" data-author-name="Bl1th">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621249">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621249/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="156">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621249"></div>
		<div class="reply-form" data-post-id="4621249"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621255">
		<a id="157" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#157</div>
			
			<i class="post-header-flag flag mod-cn" title="China"></i> 
			<a href="/user/bubzkji" class="post-header-author  mod-vlr">
				bubzkji			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621255" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>emea is the worst region haha</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:22 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621255" data-author-name="bubzkji">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621255">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621255/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="157">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621255"></div>
		<div class="reply-form" data-post-id="4621255"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621272">
		<a id="158" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#158</div>
			
			<i class="post-header-flag flag mod-ng" title="Nigeria"></i> 
			<a href="/user/big_nick_dig69" class="post-header-author  mod-vlr">
				big_nick_dig69			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621272" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>whats the point of a super team when you have Kicks? completely lost at this level </p>
<p>put him on t2 team performance be the same</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:23 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621272" data-author-name="big_nick_dig69">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621272">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621272/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="158">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621272"></div>
		<div class="reply-form" data-post-id="4621272"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621286">
		<a id="159" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#159</div>
			
			<i class="post-header-flag flag mod-id" title="Indonesia"></i> 
			<a href="/user/Jaox-101" class="post-header-author  mod-vlr">
				Jaox-101			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/466/boom-esports"><img class="post-header-flair" src="//owcdn.net/img/629f1bdae82ab.png" title="BOOM Esports"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621286" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>it should be T1 2-0 easily</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:23 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621286" data-author-name="Jaox-101">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621286">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621286/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="159">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621286"></div>
		<div class="reply-form" data-post-id="4621286"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621294">
		<a id="160" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#160</div>
			
			<i class="post-header-flag flag mod-br" title="Brazil"></i> 
			<a href="/user/fratiz" class="post-header-author  mod-vlr">
				fratiz			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621294" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>KKKKKKKKKKKKKKKKKKKK VIT NEM TROCO, PQP</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:23 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621294" data-author-name="fratiz">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621294">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621294/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="160">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621294"></div>
		<div class="reply-form" data-post-id="4621294"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621353">
		<a id="161" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#161</div>
			
			<i class="post-header-flag flag mod-id" title="Indonesia"></i> 
			<a href="/user/Ch1Lz" class="post-header-author  mod-vlr">
				Ch1Lz			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/14/t1"><img class="post-header-flair" src="//owcdn.net/img/62fe0b8f6b084.png" title="T1"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621353" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>MEMEA 🤡🤡</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:26 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621353" data-author-name="Ch1Lz">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621353">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621353/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="161">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621353"></div>
		<div class="reply-form" data-post-id="4621353"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621413">
		<a id="163" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#163</div>
			
			<i class="post-header-flag flag mod-th" title="Thailand"></i> 
			<a href="/user/VLRTHANCS2" class="post-header-author  mod-vlr">
				VLRTHANCS2			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-1"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/474/team-liquid"><img class="post-header-flair" src="//owcdn.net/img/640c38262824c.png" title="Team Liquid"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621413" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>3-0 EZ</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:30 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621413" data-author-name="VLRTHANCS2">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621413">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621413/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="163">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621413"></div>
		<div class="reply-form" data-post-id="4621413"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621414">
		<a id="164" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#164</div>
			
			<i class="post-header-flag flag mod-ph" title="Philippines"></i> 
			<a href="/user/SiriusIXX" class="post-header-author  mod-vlr">
				SiriusIXX			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621414" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>EMEA GOT HUMBLED FRFR</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:30 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621414" data-author-name="SiriusIXX">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621414">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621414/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="164">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621414"></div>
		<div class="reply-form" data-post-id="4621414"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621500">
		<a id="165" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#165</div>
			
			<i class="post-header-flag flag mod-ch" title="Switzerland"></i> 
			<a href="/user/Fonduebread" class="post-header-author  mod-vlr">
				Fonduebread			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/16806/rankers"><img class="post-header-flair" src="//owcdn.net/img/676794acc1f6d.png" title="RANKERS"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621500" data-frag-status="neutral">
					<div class="post-frag-count positive">
						2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>What a banger first map and then utter demolition in the other two ... Well fckin played by the T1 guys, individual masterclass by each one of them</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:36 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621500" data-author-name="Fonduebread">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621500">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621500/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="165">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621500"></div>
		<div class="reply-form" data-post-id="4621500"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621653">
		<a id="168" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#168</div>
			
			<i class="post-header-flag flag mod-il" title="Israel"></i> 
			<a href="/user/pemodol" class="post-header-author  mod-vlr">
				pemodol			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/13565/3"><img class="post-header-flair" src="//owcdn.net/img/6519caa187408.png" title=":3"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621653" data-frag-status="neutral">
					<div class="post-frag-count negative">
						-2 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>should put zywoo on the team</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 8:49 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621653" data-author-name="pemodol">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621653">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621653/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="168">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621653"></div>
		<div class="reply-form" data-post-id="4621653"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4621795">
		<a id="170" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#170</div>
			
			<i class="post-header-flag flag mod-br" title="Brazil"></i> 
			<a href="/user/shzuo" class="post-header-author  mod-vlr">
				shzuo			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
									<div class="star mod-3"></div>
							</div>

											<a href="/team/7386/mibr"><img class="post-header-flair" src="//owcdn.net/img/632be767b57aa.png" title="MIBR"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4621795" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Ridículo.</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 9:02 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4621795" data-author-name="shzuo">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4621795">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4621795/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="170">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4621795"></div>
		<div class="reply-form" data-post-id="4621795"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4622178">
		<a id="174" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#174</div>
			
			<i class="post-header-flag flag mod-au" title="Australia"></i> 
			<a href="/user/TYG759" class="post-header-author  mod-vlr">
				TYG759			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

											<a href="/team/8185/drx"><img class="post-header-flair" src="//owcdn.net/img/63b17ac3a7d00.png" title="DRX"></a>
			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4622178" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>So you're telling me that T1 threw map 1 just so they can destroy Vitality on maps 2 and 3??? I can't believe this T1 team man.</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Feb 28, 2025 at 10:10 PM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4622178" data-author-name="TYG759">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4622178">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4622178/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="174">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4622178"></div>
		<div class="reply-form" data-post-id="4622178"></div>
	</div>
</div></div><div class="threading"><div style="padding-bottom: 8px;">
	<div class="wf-card post    depth-0" data-post-id="4622903">
		<a id="176" class="post-anchor"></a>
		<div class="post-toggle js-post-toggle noselect">
		</div>
		<div class="post-header noselect">
			
				
			<div class="post-header-num">#176</div>
			
			<i class="post-header-flag flag mod-id" title="Indonesia"></i> 
			<a href="/user/Mobianthehero17571705" class="post-header-author  mod-vlr">
				Mobianthehero17571705			</a>

				


			
				

			<div class="post-header-stars">
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
									<div class="star mod-0"></div>
							</div>

			
			<div class="post-header-children">
			</div>
			
							<div class="post-frag-container" data-post-id="4622903" data-frag-status="neutral">
					<div class="post-frag-count neutral">
						0 
					</div>
					<b>Frags</b>
					
					<div class="post-frag-btn plus noselect " data-frag-action="plus">
						+
					</div>
					<div class="post-frag-btn minus noselect " data-frag-action="minus">
						&ndash;
					</div>
				</div>
					</div>
		<div class="post-body">
			
			<p>Gg t1</p>		</div>

		<div class="post-footer">
			<div>
				
				
				posted
				<span class="js-date-toggle" title="Mar 1, 2025 at 3:14 AM IST">
					 2 days ago				</span>
				
							</div>



		
			

			<div style="flex: 1;"></div>
			
			<div class="noselect">
								
								
															<a class="post-action reply-btn" data-post-id="4622903" data-author-name="Mobianthehero17571705">reply</a>
										<span class="post-action-div">&bull;</span>
				
				
											<a class="post-action report-btn" data-post-id="4622903">report</a>
					
					<span class="post-action-div">&bull;</span>
								
				<a href="/post/4622903/t1-vs-team-vitality-champions-tour-2025-masters-bangkok-lr1" class="post-action link" data-post-num="176">link</a>
			</div>
		</div>

		<div class="report-form" data-post-id="4622903"></div>
		<div class="reply-form" data-post-id="4622903"></div>
	</div>
</div></div></div>

<div class="report-template">
	<div class="report-form-inner">
		<form action="/post/report" method="post">
			<div class="report-form-reason">
				<div>
					<input type="radio" value="racism" id="racism" name="reason" required>
					<label for="racism">Racism/Discrimination</label>
				</div>
				<div>
					<input type="radio" value="politics" id="politics" name="reason" required>
					<label for="politics">Politics</label>
				</div>
				<div>
					<input type="radio" value="harassment" id="harassment" name="reason" required>
					<label for="harassment">Harassment</label>
				</div>
				<div>
					<input type="radio" value="content" id="inappropriate" name="reason" required>
					<label for="inappropriate">Inappropriate Content</label>
				</div>
				<div>
					<input type="radio" value="toxicity" id="toxicity" name="reason" required>
					<label for="toxicity">Excessive Toxicity</label>
				</div>
				<div>
					<input type="radio" value="advertising" id="advertising" name="reason" required>
					<label for="advertising">Advertising</label>
				</div>
				<div>
					<input type="radio" value="other" id="other" name="reason" required>
					<label for="other">Other</label>
				</div>
			</div>
			<input type="submit" value="Submit Report" class="btn mod-action">
			<input type="hidden" name="post_id" value="">
			<input type="hidden" name="token" value="1448d8ebcaa1a40802791433a4c930a9">
		</form>
	</div>
</div>

<div class="reply-template">
	<div class="reply-template-inner">
		<form action="/post/reply" method="post">
			
						<div class="post-editor mod-inset">
	<ul class="post-editor-header noselect">
		<li class="post-editor-header-action" title="Bold (Ctrl-B)" data-action="bold"><i class="fa fa-bold"></i></li>
		<li class="post-editor-header-action" title="Italic (Ctrl-I)" data-action="italic"><i class="fa fa-italic"></i></li>
		<li class="post-editor-header-action" title="Strikethrough (Ctrl-S)" data-action="strikethrough"><i class="fa fa-strikethrough"></i></li>
		<li class="post-editor-header-action" title="Heading (Ctrl-H)" data-action="heading"><i class="fa fa-font"></i></li>
		<li class="post-editor-header-action mod-link" title="Link" data-action="link"><i class="fa fa-link"></i></li>
		<li class="post-editor-header-action" title="List" data-action="list"><i class="fa fa-list-ul"></i></li>
		<li class="post-editor-header-action" title="Ordered List" data-action="olist"><i class="fa fa-list-ol"></i></li>
		<li class="post-editor-header-action" title="Quote" data-action="quote"><i class="fa fa-quote-right"></i></li>
		<li class="post-editor-header-action" title="Code" data-action="code"><i class="fa fa-code"></i></li>
		<li class="post-editor-header-action" title="Spoiler" data-action="spoiler"><i class="fa fa-exclamation-triangle"></i></li>
		<li class="btn mod-action post-editor-header-preview">Preview</li>
		<li class="btn mod-action post-editor-header-edit">Edit</li>
	</ul>
	<textarea maxlength="8000" name="body" class="post-editor-text" required tabindex="1"></textarea>
	<div class="post-loading">
		<i class="fa fa-spinner fa-spin"></i>
	</div>
	<div class="post-preview">
	</div>
</div>						<div class="form-hint" style="margin: 5px 0 0 0">
				&rsaquo; check that that your post follows the <a href="/s/rules" target="_blank">forum rules and guidelines</a> or get
				<a href="/s/formatting" target="_blank">formatting help</a>
			</div>
			
			<input type="hidden" name="parent_id" value="">
			<input type="hidden" name="thread_id" value="449012">
			<input type="hidden" name="token" value="1448d8ebcaa1a40802791433a4c930a9">
			<input type="submit" value="Reply" style="margin-top: 10px;" class="btn mod-action" tabindex="2">
		</form>
	</div>
</div><div class="action-container">
	<div>
			</div>
	<div class="action-container-pages">
		
				
				
				<a class="btn mod-page mod-to-top" href="#top">
			<i class="fa fa-chevron-up"></i>
		</a>
			</div>
</div>
	<form action="/post/add" method="post">
	
		<div class="post-editor ">
	<ul class="post-editor-header noselect">
		<li class="post-editor-header-action" title="Bold (Ctrl-B)" data-action="bold"><i class="fa fa-bold"></i></li>
		<li class="post-editor-header-action" title="Italic (Ctrl-I)" data-action="italic"><i class="fa fa-italic"></i></li>
		<li class="post-editor-header-action" title="Strikethrough (Ctrl-S)" data-action="strikethrough"><i class="fa fa-strikethrough"></i></li>
		<li class="post-editor-header-action" title="Heading (Ctrl-H)" data-action="heading"><i class="fa fa-font"></i></li>
		<li class="post-editor-header-action mod-link" title="Link" data-action="link"><i class="fa fa-link"></i></li>
		<li class="post-editor-header-action" title="List" data-action="list"><i class="fa fa-list-ul"></i></li>
		<li class="post-editor-header-action" title="Ordered List" data-action="olist"><i class="fa fa-list-ol"></i></li>
		<li class="post-editor-header-action" title="Quote" data-action="quote"><i class="fa fa-quote-right"></i></li>
		<li class="post-editor-header-action" title="Code" data-action="code"><i class="fa fa-code"></i></li>
		<li class="post-editor-header-action" title="Spoiler" data-action="spoiler"><i class="fa fa-exclamation-triangle"></i></li>
		<li class="btn mod-action post-editor-header-preview">Preview</li>
		<li class="btn mod-action post-editor-header-edit">Edit</li>
	</ul>
	<textarea maxlength="8000" name="body" class="post-editor-text" required tabindex="1"></textarea>
	<div class="post-loading">
		<i class="fa fa-spinner fa-spin"></i>
	</div>
	<div class="post-preview">
	</div>
</div>		<div class="form-hint" style="margin: 5px 0 0 0">
			&rsaquo; check that your post follows the <a href="/s/rules" target="_blank">forum rules and guidelines</a> or get
			<a href="/s/formatting" target="_blank">formatting help</a>
		</div>
		
		<input type="submit" value="Submit Post" style="margin-top: 12px;" class="btn mod-action" tabindex="2">
		<input type="hidden" name="parent_id" value="">
		<input type="hidden" name="thread_id" value="449012">
		<input type="hidden" name="token" value="1448d8ebcaa1a40802791433a4c930a9">
	</form>
					</div>
																																																			</div>
			
		
			
	<div class="media-vw">
	</div>
</div>
<div>
	<script>
		window['nitroAds'].createAd('anchor-mobile-bottom', {
		  "refreshLimit": 0,
		  "refreshTime": 30,
		  "format": "anchor",
		  "anchor": "bottom",
		  "anchorPersistClose": true,
		  "report": {
		    "enabled": true,
		    "icon": true,
		    "wording": "Report Ad",
		    "position": "top-right"
		  },
		  "mediaQuery": "(min-width: 320px) and (max-width: 767px)"
		});
	</script>
	<div id="anchor-mobile-bottom"></div>


	<script>
	window['nitroAds'].createAd('nitro-video', {
	  "refreshTime": 30,
	  "format": "floating",
	  "report": {
	    "enabled": true,
	    "icon": true,
	    "wording": "Report Ad",
	    "position": "top-left"
	  },
	  "mediaQuery": "(min-width: 1840px)"
	});
	</script>

<div class="footer">
	<div class="footer-inner">
		<div class="header-div mod-first"></div>

			<a href="mailto:community@VLR.gg" class="contact">Contact</a>
			<div class="sdot">&bull;</div>
			<a href="/privacy" class="privacy">Privacy</a>
			<div class="sdot">&bull;</div>
			<a href="/terms" class="privacy">Terms</a>
			<div class="sdot">&bull;</div>

							<a href="/user/view/desktop">
					Switch to Desktop
				</a>
			
	
			<div class="find-txt">
				Find us on:
			</div>
			
							<a href="https://twitter.com/vlrdotgg" target="_blank" class="social mod-twitter">
					<i class="fa fa-twitter mod-twitter"></i>Twitter
				</a>
						
							<a href="https://discord.com/invite/VLR" target="_blank" class="social mod-discord">
					<img src="/img/icons/social/discord.svg" class="mod-discord">Discord
				</a>
						
			
			
		<div class="header-div mod-last"></div>
	</div>	
</div>	<script src="/js/common/vendor/jquery.min.js"></script>
<script src="/js/common/main.min.js?v=73"></script>

	<script src="/js/common/match.js?v=22" ></script>
	<a id="bottom"></a>
</body>
</html>
    """  # Replace with actual HTML content

    extracted_map_data = extract_map_data_detailed_page_attempt_29(detailed_page_source_code) # Use Attempt 29 function

    print("\nAttempt 29 - Extracted Map Data (Specific Maps, No Overview, Cleaned Names, Team Names v3 - .team-name):") # Output message updated
    if extracted_map_data: # Check if map_data is not empty
        first_map_item = extracted_map_data[0] # Get the first map item to dynamically get team names
        team1_key = list(first_map_item.keys())[1] # Get the second key (first team name) dynamically
        team2_key = list(first_map_item.keys())[2] # Get the third key (second team name) dynamically

        for map_item in extracted_map_data:
            print(f"Map: {map_item['map_name']}, {team1_key}: {map_item[team1_key]}, {team2_key}: {map_item[team2_key]}") # Use dynamic team name keys in output

    else:
        print("No map data extracted.") # Handle case with no map data

    print(f"\nAttempt 29 - Total Maps Found (Specific Maps, Cleaned Names, Team Names v3 - .team-name): {len(extracted_map_data)}") # Output message updated