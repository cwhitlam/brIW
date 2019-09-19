import os

danny = """
XXKKK00OOOOOOOOOO0000KKKKK000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKKKKKKKKKKXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNX
XXXXXKKKK00000000000KKKKK0000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKKKKKKKKKKXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
XXXXXXKKKK00000000000KK000000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKKKKKKKKKKXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
XXXXKKKKKKK000000000000000000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKKKKKKKKKXXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
KKKKKKKKKKK000000000000000000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKKKKKKKKXXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
00000000000000000000000000000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKKKKKKKXXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
00000000000OOOOOO000000000000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKXXXKKKKKKKKKKKKKKKXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
OOOOOOOOOOOOOOOO00000000000000000000000000KKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKXXXXXXXXXXXXKKXXKKKKKKKKKKKKKKKXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
kkkkkkkkOOOOOOO0O000000000000000000OOO0000KKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXKK0OOkkkkkkkkkkkkkOOO000KKKKXKKKKKKKKKKKKKKKXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
kkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO000KKKXXXXXXXXXXXXXXXXXXXXXXXXXKOkkxxxxxxxxxxxxkkxxxdddxxxxxxkkOOO00KKKKKKKKKKXXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
kkkkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOO000KKKXXXXXXXXXXXXXXXXXXXXXK0kxdddxxxxxxxxxxxxxxkxxxxxxxxxxddddddddxxkO00KKKKKKXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
xxxxxxxxxxkkkkkkkkkkkkkkkkkkkkOOOOkkOOO000KKKXXXXXXXXXXXXXXXXXXK0kxdoodxxxxxxxxxxkkxxxkkkxxxxddddddddddddddddddxkkO0KKKKKKKXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
ddxxxxxxxxxxxxxxxxxxxxxkkkxxkkkkkkkkOOO00KKKKXXXXXXXXXXXXXXXK0kdddddddxxxxxxxxxxxkkkkkkkkkxxxxxxxxddddddddooooooooodkO00000KKXXXXNXNNNXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
dxxxxxxdddxxxxdddddddddxxxxxxxxkkkkkkOO00KKKKXXXXXXXXXXNNX0kdoooodddddxxxxxxxxxkkkkkkkkkkkkkkxxxxxxxxxxddddoodoooooooodxxkO000KKXXXXXXKKKXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
dxxxxxxxdxxxdddddddddddxxddddxxxxxxkkOO000KKKXXXNXXXXNXKOxoooooddddddddxxdddxxxxxkkkkkkkkkkkkxxxxxxxxxxdddddddoooooooooloodxkO000O00KKKKKKKKKKXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
xxxxxxxxxxxxdddddddddddxxddddxxxxxxkkOO000KKKXXXXNXNNXOdlloooodddddddddxxxxxxxkkkkkkkkkkkkkkkkkkxxxxxxxdddddddddddddooooooooooddddxkkkkkOOO000KKKXXXXXXNNNNNXXNNNNNNNNNNNNNNNNNNNXXXNNNNNNNNNNNNNXXXXXXX
kkkkkkkkkkkkxxxxxxxxxxxxxxxxxxkkkkkkkOO00KKKKXXXXXNX0dlclloooddddddxxxxxxxkkkkkkkkkkkkkkkkkkkkkkkkxxxxxxddddddddddddoooooooolllcccccc::ccloooodxk00KKKXXXXXXXXXXXXXXNNNNNNNNNXXXXXXXXXXXXXXXXXXXXXXXXXXX
OOOOOOOOOOOOOkkkkkkkkkkkOOOOOOOOOOOOO000KKKKKXXXXX0xlccllloddddddddddxxxxxxkkkkkkkkkkkkOkkkkkkkkkkxxkkxxxxxdddddddddooooooooloolc:;,,',;:::::::clodxO00KKKKKKKXXXXXXNNNNNNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXX
00000000000000000000000000000000000000KKKKKKXXXXKklccccllooddddxxxxxxxxxxkkkkkOOOOOOkkOOOOOOkkkkkkkkkkkxxxxxxddddddddoooooooollllc;,'......',;;::cllldxkOOO0KKKKKKKKXXNNNNNXXXXXXXXXKKKKXXXXXXXXKKKKKXXX
KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOdc:ccclloodddxxxxxxxxxxxxxkkkkkkkkkkkkkkOkkkkkkkkkkkkkkxxkxxxxxxdddddooodddddoollc:;,'...........,:::;:loxkO000000KKKXXXXXXXXKKKKKKKKKKKKKKXXXKKKKKKKKKK
KKXXXXXXXXXXKKKKXXXXXXXXXXXXXXXXXXXXXKKKKKK00Okl:::cccloooddddxxxxxxxxxxkkkkkkkkOOOOOOOOOOkkkkkkkkkkxxxkkkxxxxxxxxddddddddddddoolc:;;,'............';;,,;codxkkO00K00KKKKXKKKKKKK00000000000KKKK00000000
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKK000Okdl::::cccloooddddxxxxxxxxkkkkkkkkkkOOOOOOOOkkkkkkkkkkkkkkkxxxxxxxxxxxxdddddddddddddol:;,,,,'.........  ....',cllldxxkOOO0OO0KKKK0000000OOOOOOOO00000000000O
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKK00Oxollc:::::ccclloodddxxxxxxxxkkkkkkkkkkkkkkkkkOOkkkOOOkkkkkkkkkkkkxxkkkxxxxxdddddddddddool:;;;;,'....           ...,:clloxxkkkkxkO000000OOOOOOOOkkkOOOOOOOOOOOOO
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKOxdl:;;:c:::::ccccloodddxxxxxxxxkkkkkkkkkkkkOOOkkOOOOOOOOOOOOOOOkkkkkkkxxkkkxxxdddddddddddolcccc:;,''....               ..,:lodxxkkxddkO0OOOOOOOkkkkkkkkkkkkOOOOOOOk
XXXXXXXXXXXXXXXXXXXXXXXXNXXXXXXXX0kxo:,',;ccc::::::clooooddxxxxxxxkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOkkkkxxxxxxkkxxxdddddddoooolccc::;,,'....          ...    ..;cclddxxdddxkOOOOOOkkkkkkkkkxxxkkkOOkkkk
XXXXXXXXXXXXXXXXXXXXXXXXNXXXXXXK0xooc;,,;clcc::::ccllooddxxxxxxxxxkkOOOkkkkOOOOOOOOOOOkkkxxdddddddxxxxxxxxxxxxxxxxxxddxxxddoooolcc:;,,,,'....           ....   ..';clodddddodxkOOOkkxxdxxxxxxxxxkkkOOOkk
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0ko:,'',;cclccc:::clloodddxxxxxkxxxxkOOOOkkOOOOOOOkkxxxxdoc:;,;;;;;;:ccccllldxxxxxxxxxxxxxxdddollcc;,',,''....              ....   ..,:lodddddddxkkkkxdddxxkkkkkkkkOOOOOk
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKkl,..',;:cccccccclllloolllooooddddddxkOOkkkOOOOOkkxxxxxxdlc:,'''....'',,,,,,'',,,,;:ccloxkxxddolllc;,,''''.....            ........  ...,;:codddddddddddxxkkkkkkkkkOOOOOk
XXXXXXXXXXXXXXXXXXXXXXXXXXKKKKk:.....';:cccccclolcccc;,''',;::ccloodkkkxxxkkkOkkkkxdlllcc:;,,;:ccloooooooolc:;,'..    .;c;;:llllc:;,,'',,'....              ................';coddolllodxkkkkkkkkkkkkkkk
XXXXXXXXXXXXXXXXXXXXNXXXXKKKOd:'.....,::ccccccllc;'..........',,:clodxxxkkkkkkxoc,..':cclooddxkxxxxkkkkkxxdxxxddl:,.   ..    ..',,,,''','.....               .. .....',::;,,,''';cloooooxkkkkkkkkkkkkkkk
XXXXXXXXXXXXXXXXNXXXNNXNX00kl;,'....',;:cc::;,'.....................',;::cc:;'..  .;ccllcc:::::;;;;;;;;;:clcclcloodc.               ..',.......                 ......',:cc:;;;;,;:llodddkOOkkkkkkkkkkkk
XXXXXXXXXXXXXXXNNXXXXNNXXKOd:;,'. ...''''.......',:ccclllllllcc:,'..            .',,,''',;;;:cclloolcc:;;:;;;:clc;cl'                     ...                   ..........,;:;',;,;cllodxkkOOkkkkkkOOOOk
XXXXXXXXXXXXXXXNXNNXXXNXX0kc:;,....      ..',,;cllllc:;:;;;;:::::;,'.           .,'..';:ccclolllccllloooolc:coddoccl,                                              .........;:,',;,,:ccoxkkOOkkkkkOOOOOO
XXXXXXXXXXXXXXXNXXNXXXXXXKkl:;.  ..    .,,'';::;;;'.....'',,;;;;:;;;.          .::;,,;:cc:;;,'...'....,:;,,;coddollc'                          ..                   ....'....','..'',;:oxkkkkkkkkkOOOOOO
XXXXXXXXXXXXXXXNXXNXXXXXXXkc:'.   .   .,;,'',;,''...';::::;;;;,,,,,,'.         'll:;;;;;;'':c;..'',;;,:c:;:ldolcccc;. ...                                            ....'''. ....''',;ldxxxxxxkkkkOOOOk
XXXXXXXXXXXXXXXXXNNNXXXXXXxc;.    .   .,,'..',,'.',,,,'... ........''.    .''.  .;llcll:;;:lol::lodxxxkkxxdddollccc'  ............              ...'...               .............',,,;coodxxxxkkkkkkkk
XXXXXXXXXXXXXXXNNNXXNXKKK0xo:..   ..  ......';,'''.....''...''...'',;.  .,cooc'  .cddxdoloooooodxxxxxxxxddddxdocclc'.';;:::::::::;,'...        .........              .... ..........,,,;clldxkkkkkkkkkk
XXXXXXXXXXXXXXXNNXXNXKkkOkkx;.    ..  ......';::ccccclllllllooolc:;;;.  .cdxxxo,. .lxxxdoolooooddddooolodxkkkkdoloc..ldllllolccclc:;,'...      .........               ..........  ..',,;ccldxkkOOkkkkxx
XXXXXXXXXXXXXXXXXNNXX0kkO0Od;..   ..  ......';;;;:clddddddoooollc::l:. .;ldxxxxdc..'lxkkkxdlcccccclooodxkkkkOkxodd:.;dxdolllllllllcc;,....    ....'...,'.        .     ...........  .',,:::ldxkkkkkkxxdd
XXXXXXXXXXXXXXXXNNXXXXK00Oxl;,,.   .   ....,;:::::clloooollcc::cllll:. ,odxxxxxxxo,.'lxkkkkkkxddoddxkkkkkkkkkkkkxl''oxxxxxdooooolc:,....... ...';cc;;:l:.        .........',;,..... .','.,:dxxxkxxxxddol
XXXXXXXXXXXXXXXXXXXXXKK0kddlcc;.        .'',;:ccloooddddddoooodddool'.,oddxxxxkkxkx:..cxkkOOkOkkkkkkkkkkkO00O0Oxc',okxxxxkxxddddooc:,..........':lolccol.            .....';ll,......',;:oxkkxkkxxdoollc
XXXXXXXXXXXXXXXXXXXXXK0Oxdolc:'.        ..';:::cloodxxkkkkkxxxxxdol,..cdddxxxxkkkkkxl,.,:lddxkkkkkkxxkkkkkkxol:,':oxxkkkkkkkxdddddoolc:;,''...',:clc:ldl.             ......;c;'',,,';::codxxxxxddollc:;
XXXXXXXXXXXXXXXXXXXXXK0Okxdoc,'..     .. .';:cloodxxkOOOOOkkkkkxoc'..,lddxxxxxkkkkxdool;,''..,;;:;;;;;;;;;;;;;:ldxxxxkkOOkkkkxddddooooooc:;,,'.,:llcccol'              ......';,,;;,;loolooooddollc:;;,'
XXXXXXXXXXXXXXXXXXXXXK0Oxdl:;,;;..    .....,:lloddxxkkkkkkkkkkdc'.':clloddxxkkkkkkxddxkkkxo;......,:cclooxxkOOOOkkkkkxkkOOkkkxdddoodddddolc:cc;';cllllll' ...           .......';;:;:::clolc:ccc:;,''''.
XXXXXXXXXXXXXXXXXXXXK0Okdlclccl:,......','..';cloddddxxxdolc:,...;ddlcclddxxkOOkkxdddxkOOkkdc:ccc::ccloxkkkkkOOOkkkxxxxkkkkkkxxxdooddddddolcldoc:llodooc.                 ... ........,cllc:;;;,,''..'',
XXXXXXXXXXNNNXXXXXXXK0Okoldxdoo:'.''...';::,.....''''''''.......,cllc;;:codddddoooooddddooooccdxxdlc:;;:cldxxxkkkxxxxxxxxkkkkxxxdddxxxkxxddoloollooodxo:.                       ......',,,''''''..''',;;
XXXXXXXXXXXXXXXXXXXXXK0kox0kxxo:'';:;,.'::::;,',,;:::cccc:,,,;;;;,,,'..',:cllllccc:,''...',:coxkkkxxddl:;;:codddxxxxxxxxxkkkkkxxxxxxxxkkxxddoollooooddl'                        ..,;;,''........'',,;;::
XXXXXXXXXXXXXXXXXXXXXKKkoxkkxxo:';:::;',::::::clodddddoc:;:llc::;'........',;:cc:;,'',,,;:coxkkkkkkxxxxdoc;,,:loddddxxxxxkkkkkkxxxxxxxxxxxxdddolldxdol;.                   ...   .,,,,,'.......''',,;::c
XXXXXXXXXXNNXXXXXXXXKK0Oxdxkxxo:,;,,,,;:::::::cllllol:;,;cllcc::::;,,'''.....',,,;:loooodxxxkkkxxxxkkxxdddoc;,,;lodxxxxxxkkkkkkxxxxxxxxxxxxxdddoloxxoc,                     ..   .'''''......'''',,;::cl
XXXXXXXXXXXXXXXXXXXXXK0Oxxkkdo:,;;',colc::::;:cllllc;,,:cllllcc::::::::;;;,'''',:loxxxxxxxxxxxxddddxxkkkxxxddl:;:ldxxxxxxkkOkkkkxxxxxddddxxxxddolloxkd;.                     .   ......''''',,,,;;::ccll
XXXXXXXXXXXXXXXXXXXKK0OkxkOOxoclxd;,cdo:::::;:ccllc;;:ccccllcclccccccc::ccllccloddxxxddddxxxxxdooddxxxxddddddxdlcldxxxxxkkOOOOOkkxxxdddddddxdddoolcldxl'                 ..    .....',;;;:;;;;;::cccccll
XXXXXXXXXXXXXXXXKKKKKXX0OOOkxooxOd:;ldl:::::::cclc:;:lllllllccllcclllccccloollllooooddodddddddddoooooolllooooooooodxxxxxkkkOOOOkkkxxdddoodddddddoolc::;'                 ....   ...';clcclol::cllllc::cc
XXXXXXXXXXXXXXXXXXXXXXXKK000OdoxOxllooc:::::::cllllccclllllc:::c::cllllllloolloododdddooooollccc:::::;:;;,'';;:oddxxxxxkkkkOOOOkkkxxddoooooddxxdoolc;..                  ..... ....':c:;:dxxdddddolc:;;;
XXXXXXXXNNXXXXXXXXNNXXKKKKKXKkxkOOkdoc::cccc::cloddollcc:::;;,,,''','',,,,;:;:cllccccccc:ccc:;;,....  ...';:c:coxxxxxxxkkkkOOOOkkkxddooloodddxdddoll:.                    ......',;cdxxdxOOOOOkxxdol:;,;
XXXXXXXXXXXXXXXXXXXXXXKXXXKKKOO000K0xl::cccc::cloxxxdol:;,......     .''',,,,;::;cllloxkxx0KOOOkxo;...;loddxdlloxxxxxxkkkkkkOOkkkxxdoollldxkxxddoolc:'                     ....';lxkO0KKKKKKK00Okxxolc:c
XXXXXXXXXXXXXXXXXXXXXKXXXXKKKK0K0000Oo::cclc::clodkkkxdol:;'....    .:ddxkkxkO0OkOKXK000kooxdlodxxollodxxxxxxdooxxxxxkkkkkkkOOkkxxddolclodxxxxxddocc:'                       ...;ok0KKKXXXXXXKK0OOkxdddd
XXXXXXXXXXXXXXXXXNXXXXXXXXK0KKK0000K0o::ccllccclloxxkkxxdddl:::;,....:lc:ldxxkkkkkkkdolllc:ccccloddxxxxxxkxxxdxxxxxxxxkkkkkOOOkxxdoolccldxxxxxxddocc:.                    ..... .;kKXXNNNNNXXXKK00OOkkkk
XXXXXXXXXXXXXXXXXXXXXXXXXXKKKXKKKKKK0d:;:cclllcloodxxxxxxxdollllll:::;;,,;cllooddddxdxxkkkkxxxxxxxxxxxxkkkxxxxxkxxxxxxxkkkkkOkkxdoolccloxkkxxxddolc:,.               ..   .:c;..;xXNNNNNNNNNNXXKKKK000OO
XXXXXXXXXXXXXXXXXXXXXXXXXXKKKXXKKKKKKk:,;:::clllooodxxddddddoollllllccclodddxxxxxkkxxxkkkkkkkkxxxxxxxxkkxxxxxkxxxddxxxxkkkkkkkxdoollcloxxxxxxxollc:,.                ...  .cxkxk0XNXNNNNNNNNNNXXXXXKKK00
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKXKX0o,';::cllloooodddddddooooolcccclloooddxxxxxxkkxxkkkkkkkkkkkkxxxkkxxxxkkkkxxdddxxxxkkkkxxdolllcloxxxxxxddolc;,,.                ....,lxO0KKXXXXXXNNNNNNNNNXXXXXKKKK
XXXXNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXKXXOc'',;:ccllooooodddoooollll:::clllooddxxxxxxkkxxkkkkkkkkxxxxxxxxxxxxkkkkxxxddxxxxxkkkxddollccloxxxxxddool:;,,,.                .  .ok000KXNNXXXXNNNXNNNNXXXXXKKKKK
XXXXXXXXXXXXXXXXXXXXNNNXXXXXXXXXXXXXKKXk;..,;::cllooodoooooooolccc::ccllodddddxxxxkkkkkkkxxkkkxxxxxxddxxxkkkkxxdddxxxxxkkxxdollccclodxxdddooc::;;,,,.                .. .o0KKKOxdl:;:codolllllcc::::;;::
NXXXXXXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXKKXXd'..';;:ccloooolloooooollcc:::cllooodddxxxkkkkkkkkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkxdollc:::ldxxdddoolc::;,,,,..           .    ..  .:ll:.....  ...................
NXXXXXXXXNNNNNNNNNXXXXXXXXXXXXXXXXXKKKKXKl....';;:clooolccllooooollllllloooddxxxxxkkkkkkkkxxxxxxxxxxxxxxxxxdddxxxxkxxxxddolc::::loddooollc::;,,,,,..            .. .... .....  .........................
NXXNNNNNNXXK0OOO0KXNNNNNNNXXXXXKXXKKKKKXX0c....',;:cloolc:::clllooooollllooddxxxxxxxkkkkxxxxxxxxxxxxxxxxddddddxxxkkkxxdoc::;;clooooollcc:;;,',;;....       .   ...  ....................................
NNX0Okdlc;'......';cclodxkO0KXXXXKKKKXKKKX0l.....',;cclll:;;:cllllooollclodddddddddxxxxkkxxxxxxxxxxxxxxdooddxxkkkxxxddlc:;;:cloolllcc::;;,,;;;'. ..       .... .........................................
xc,...      ..           ...,:oxOKXXKKKKKKXKd'.....',:cccc::;;:cloooollc:loddddxxdxxxxxddxxxxxxddddddddolodxxxkkxxddoc::;:cloooccccc:::::::;'.            ..............................................
.          ...                 ..;lk0KKKXKKXXO:......';::cc:;;;:cllcclllccloodxxddddxkxddxxxddoooodooollodxxxxxxxdol::;:clooolcccccc:ccc:;..         .................  ................................
  ...                              .,lkKXXXXKkc. ......,;;:::::;;;:::::clllloodddoodxxxxdddolclloolc:cldxxxxxxxdooc:::clooolllcclllllc;,..    .     ............. .... .................................
  ..                                  .,:cc;..       ....',;;:::;,,,;;;;::ccccllllloolllcc::::ccc::cloxxxxxxxdollc::clooollclllloolc,...        ..  .... ... .......................................... 
 ..    .                                              .....',;:::;,,'',,,,,,,,;::::::;;;;;;;;;;;;coxxxxxxxxdoolc:ccloooolllooodol:'....... ..   ... ..................................................  
...   ..                                                  ...';;:;:;,''....'''',,,,,,,''''''';:lodxxxxxddddolcc::cloolllloooooc;.............   ... ........ ......................................... .
...  ..    .                                               ....,,;;:::;,'................',:ldxxxddddddolcc:::::cloooloooool:,..........  ......... ..                                 .............. ..
..   .  .                                                  ......',,,;;::::;;,,''''',;:cloddxdddddddoolc::;;,,;:lloooooolc;'.............. ..               ...                    ................ ....
..   .. .                                                  ... .....',,;::cclllllooodddddddddooolllcc::;,,',;:clllllool:,...............                ............  ..      ..........................
..               ..                                          ..........',;;:clllloooooolllllcccc:;,,''...,;clllllllll:'.................     ...      ........................................ .........
.             ...                                             ............',,;;::ccccccc::;;;,,'......',;:cclllccc:,'...................... ...    .......................................... ..........
.                      .                                      .................'',,,,,,,''.........',,;:ccc:::;,'............................   ........................................................
.          .                                                  ..................................',;:::::;,,'................................  .............................................. ...........
            ..                                                  . ..........................'',,,,,,,'..................................................................................................
           ...                                                 ... .....................''',,''............................................................................................ ............
           ..                                                  ......................'''.........',''...................................................................................................
            ...                                                 .'.........................',;:::,'.....................................................................................................
            ...                                                 .',,'.................',;::ccc:,........................................................................................................
"""
resize = lambda: os.system("printf '\e[8;100;200t'")


def devito_time():
    resize()
    return(danny)
