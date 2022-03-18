from rich.console import Console

console = Console()

class main:
    def helloscreen():
        console.print("""
                        _______           __       __          __   __                       
                        |       \         |  \  _  |  \        |  \ |  \                      
                        | ▓▓▓▓▓▓▓\__    __| ▓▓ / \ | ▓▓ ______  \▓▓_| ▓▓_    ______   ______  
                        | ▓▓__/ ▓▓  \  |  \ ▓▓/  ▓\| ▓▓/      \|  \   ▓▓ \  /      \ /      \ 
                        | ▓▓    ▓▓ ▓▓  | ▓▓ ▓▓  ▓▓▓\ ▓▓  ▓▓▓▓▓▓\ ▓▓\▓▓▓▓▓▓ |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\\
                        | ▓▓▓▓▓▓▓| ▓▓  | ▓▓ ▓▓ ▓▓\▓▓\▓▓ ▓▓   \▓▓ ▓▓ | ▓▓ __| ▓▓    ▓▓ ▓▓   \▓▓
                        | ▓▓     | ▓▓__/ ▓▓ ▓▓▓▓  \▓▓▓▓ ▓▓     | ▓▓ | ▓▓|  \ ▓▓▓▓▓▓▓▓ ▓▓      
                        | ▓▓      \▓▓    ▓▓ ▓▓▓    \▓▓▓ ▓▓     | ▓▓  \▓▓  ▓▓\▓▓     \ ▓▓      
                         \▓▓      _\▓▓▓▓▓▓▓\▓▓      \▓▓\▓▓      \▓▓   \▓▓▓▓  \▓▓▓▓▓▓▓\▓▓      
                                |  \__| ▓▓                                                   
                                \▓▓    ▓▓                                                   
                                 \▓▓▓▓▓▓ 
                                                                                            
""", style="#ffa407")
        from colorama import Fore, Style
        print(Fore.CYAN + "\t\t\t\t\t\t\t\t made by " + Fore.LIGHTMAGENTA_EX + "@PhiPei7" + Fore.CYAN + ", " + Fore.LIGHTMAGENTA_EX + "@kandi-ist-opa\n\n\n" + Style.RESET_ALL)
