"""
OmniBox - One Tool, Infinite Possibilities

A powerful AI-powered CLI utility with voice support.
Supports natural language commands in both Hindi and English.

Usage:
    python main.py              # CLI mode (default)
    python main.py --voice      # Continuous voice mode
    python main.py --help       # Show help

Author: Yashasvi Yadav
GitHub: github.com/YASHASVIYADAV30/omnibox
License: MIT
"""

import sys
import os
import argparse

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Fore:
        CYAN = MAGENTA = YELLOW = GREEN = RED = BLUE = WHITE = ""
    class Style:
        RESET_ALL = BRIGHT = ""

from core.assistant import OmniBox
from core.speech import speak, listen
from utils.config import Config


# App version
VERSION = "1.0.0"


def clear_screen():
    """Clear terminal screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_banner():
    """Display OmniBox ASCII art banner."""
    banner = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║      ██████╗ ███╗   ███╗███╗   ██╗██╗██████╗  ██████╗ ██╗  ██╗║
║     ██╔═══██╗████╗ ████║████╗  ██║██║██╔══██╗██╔═══██╗╚██╗██╔╝║
║     ██║   ██║██╔████╔██║██╔██╗ ██║██║██████╔╝██║   ██║ ╚███╔╝ ║
║     ██║   ██║██║╚██╔╝██║██║╚██╗██║██║██╔══██╗██║   ██║ ██╔██╗ ║
║     ╚██████╔╝██║ ╚═╝ ██║██║ ╚████║██║██████╔╝╚██████╔╝██╔╝ ██╗║
║      ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝║
║                                                               ║
║            📦 One Tool, Infinite Possibilities 📦             ║
║                   AI-Powered Utility Suite                    ║
║                        v{"1.0.0"}                               ║
╚═══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """
    print(banner)


def print_help():
    """Display command reference guide."""
    help_text = f"""
{Fore.YELLOW}╔═══════════════════════════════════════════════════════════════╗
║                     📋 COMMAND REFERENCE                       ║
╚═══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.CYAN}🌐 WEB & SEARCH{Style.RESET_ALL}
   open youtube / google / github    Open popular websites
   open <website>                    Open any website
   search <query>                    Search on Google
   play <video> on youtube           Play video on YouTube

{Fore.MAGENTA}🎵 MEDIA & MUSIC{Style.RESET_ALL}
   play music                        Open music player
   play lofi / bollywood             Play mood-based music
   play <song name>                  Play song on YouTube

{Fore.GREEN}💻 APPS & SYSTEM{Style.RESET_ALL}
   open notepad / calculator         Open system apps
   open vscode                       Open VS Code
   open downloads / documents        Open system folders
   screenshot                        Take a screenshot

{Fore.YELLOW}🌦️  INFORMATION{Style.RESET_ALL}
   weather <city>                    Get weather info
   news                              Get top headlines
   time                              Current time
   date / today                      Current date

{Fore.BLUE}🎙️  VOICE CONTROL{Style.RESET_ALL}
   voice on                          Start voice mode
   voice off                         Stop voice mode
   voice                             Single voice command

{Fore.RED}⚡ GENERAL{Style.RESET_ALL}
   help                              Show this help
   clear                             Clear screen
   exit                              Exit OmniBox

{Fore.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 TIP: Speak naturally! Try: "Play Arijit Singh on YouTube"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Style.RESET_ALL}
    """
    print(help_text)


def clean_for_speech(text: str) -> str:
    """Remove emojis and special characters for cleaner speech output."""
    emojis = [
        "🎬", "🔍", "📦", "🌐", "📁", "💻", "🎵", 
        "🌦️", "📰", "🕐", "📅", "🤖", "📸", "📚", 
        "🔌", "🔄", "🔒", "👋", "✨", "🎤", "⚡"
    ]
    for emoji in emojis:
        text = text.replace(emoji, "")
    return text.strip()


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="OmniBox - AI-Powered Utility Suite",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py              Start in CLI mode
  python main.py --voice      Start in voice mode
  python main.py --version    Show version
        """
    )
    
    parser.add_argument(
        '-v', '--voice',
        action='store_true',
        help='Start in continuous voice mode'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f'OmniBox v{VERSION}'
    )
    
    return parser.parse_args()


def run_cli(omnibox: OmniBox, voice_mode: bool = False):
    """
    Run the main command loop.
    
    Args:
        omnibox: OmniBox instance
        voice_mode: Start with voice mode enabled
    """
    current_voice_mode = voice_mode
    
    # Show initial instructions
    if current_voice_mode:
        print(f"{Fore.MAGENTA}🎤 Voice mode is ON. Just speak your commands!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Say 'exit' to quit or 'voice off' to switch to typing.{Style.RESET_ALL}\n")
    else:
        print(f"{Fore.CYAN}💬 Type your commands below. Type 'help' for available commands.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}   Type 'voice on' for voice mode or 'exit' to quit.{Style.RESET_ALL}\n")
    
    # Main interaction loop
    while True:
        try:
            # Get user input based on mode
            if current_voice_mode:
                user_input = listen()
                
                if not user_input:
                    continue
                
                print(f"{Fore.CYAN}🗣️  You: {user_input}{Style.RESET_ALL}")
            else:
                user_input = input(f"{Fore.MAGENTA}┌──[{Fore.CYAN}You{Fore.MAGENTA}]\n└─> {Style.RESET_ALL}").strip()
            
            if not user_input:
                continue
            
            command = user_input.lower().strip()
            
            # Handle exit commands
            if command in ['exit', 'quit', 'bye', 'goodbye', 'close']:
                farewell = "Goodbye! Have a great day!"
                print(f"\n{Fore.CYAN}👋 {farewell}{Style.RESET_ALL}")
                speak(farewell)
                print(f"{Fore.GREEN}✨ Thank you for using OmniBox!{Style.RESET_ALL}\n")
                break
            
            # Handle voice mode toggle
            elif command in ['voice on', 'voice mode', 'start listening']:
                current_voice_mode = True
                response = "Voice mode activated. I'm listening."
                print(f"{Fore.GREEN}🎤 {response}{Style.RESET_ALL}")
                speak(response)
                continue
            
            elif command in ['voice off', 'stop listening', 'typing mode']:
                current_voice_mode = False
                response = "Voice mode disabled. You can type now."
                print(f"{Fore.YELLOW}⌨️  {response}{Style.RESET_ALL}")
                speak(response)
                continue
            
            # Handle single voice command
            elif command == 'voice':
                print(f"{Fore.YELLOW}🎤 Listening...{Style.RESET_ALL}")
                voice_input = listen()
                
                if voice_input:
                    print(f"{Fore.CYAN}🗣️  You said: {voice_input}{Style.RESET_ALL}")
                    user_input = voice_input
                else:
                    print(f"{Fore.RED}❌ Could not hear anything. Please try again.{Style.RESET_ALL}\n")
                    continue
            
            # Handle help command
            elif command == 'help':
                print_help()
                continue
            
            # Handle clear screen
            elif command == 'clear':
                clear_screen()
                print_banner()
                continue
            
            # Process command through OmniBox
            print(f"\n{Fore.YELLOW}📦 OmniBox:{Style.RESET_ALL} ", end="")
            response = omnibox.process_command(user_input)
            
            if response:
                print(f"{Fore.GREEN}{response}{Style.RESET_ALL}")
                
                # Speak the response (clean version)
                clean_response = clean_for_speech(response)
                if clean_response and len(clean_response) < 300:
                    speak(clean_response)
            
            print()  # Empty line for spacing
            
        except KeyboardInterrupt:
            print(f"\n\n{Fore.YELLOW}⚠️  Interrupted by Ctrl+C{Style.RESET_ALL}")
            print(f"{Fore.CYAN}💡 Type 'exit' to quit properly.{Style.RESET_ALL}\n")
            continue
        
        except Exception as e:
            print(f"{Fore.RED}❌ Error: {str(e)}{Style.RESET_ALL}\n")
            continue


def main():
    """Main application entry point."""
    try:
        # Parse command line arguments
        args = parse_arguments()
        
        # Clear screen and show banner
        clear_screen()
        print_banner()
        
        # Show startup mode
        if args.voice:
            print(f"{Fore.GREEN}🎤 Starting in Voice Mode...{Style.RESET_ALL}")
        
        # Load configuration
        print(f"{Fore.YELLOW}⚙️  Loading configuration...{Style.RESET_ALL}")
        config = Config()
        
        # Initialize OmniBox
        print(f"{Fore.YELLOW}📦 Initializing OmniBox...{Style.RESET_ALL}")
        omnibox = OmniBox(config)
        
        print(f"{Fore.GREEN}✅ OmniBox is ready!{Style.RESET_ALL}")
        
        # Display and speak greeting
        greeting = omnibox.greet()
        print(f"{Fore.CYAN}🤖 {greeting}{Style.RESET_ALL}\n")
        speak(greeting)
        
        # Run main command loop
        run_cli(omnibox, voice_mode=args.voice)
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
        sys.exit(0)
    
    except Exception as e:
        print(f"\n{Fore.RED}💥 Fatal Error: {str(e)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please check your configuration and try again.{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == "__main__":
    main()