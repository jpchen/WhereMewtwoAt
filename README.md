Building off of [tejado](https://github.com/tejado/pgoapi)'s Pokemon Go API. Use at your own risk.

I don't have the time right now to work on this. Maybe in  the future.

##Usage
    $ python demo.py  demo.py -u "user" -p "pw" -l "Seattle" -n Mewtwo

    [!] Your given location: Seattle, WA, USA
    [!] lat/long/alt: 47.6062095 -122.3320708 0.0
    [!] login for: testdemo123123
    [+] Received API endpoint: https://pgorelease.nianticlabs.com/plfe/120/rpc
    [+] Login successful
    [+] Username: testdemo 
    [+] You are playing Pokemon Go since: 2016-08-03 02:55:50
    [+] POKECOIN: 0
    [+] STARDUST: 0
    No Mewtwo within 143m NW of you...
    No Mewtwo within 594m NW of you...
    No Mewtwo within 594m NW of you...
    No Mewtwo within 842m NW of you...

    (150) Mewtwo is visible at (47.6070213823, -122.338763651) for 780 seconds (1042m NW from you) 

## Documentation
Documentation is available at the github [pgoapi wiki](https://github.com/tejado/pgoapi/wiki).

## Requirements
 * Python 2 or 3
 * requests
 * protobuf (>=3)
 * gpsoauth
 * geopy (only for pokecli demo)
 * s2sphere (only for pokecli demo)

## Acknowledgements
[Mila432](https://github.com/Mila432/Pokemon_Go_API), [AHAAAAAAA](https://github.com/AHAAAAAAA/PokemonGo-Map), [tejado](https://github.com/tejado/pgoapi)
