def main():

    robotpy_logo = r"""
                                                  /PPPPPPPPPPYYYYYYYYYY\       
                                                 /PPPPPPPPPPPYYYYYYYYYYY\      
                                                /PPPPPPPPPPPPYYYYYYYYYYYY\     
RRRRRR   OOOOOO  BBBBBB   OOOOOO  TTTTTTTT     /PPP       PPPY  YYYYYY  YY\    
RR   RR OO    OO BB   BB OO    OO    TT       /PPPP  PPPP   PY  YYYYYY  YYY\   
RR   RR OO    OO BB   BB OO    OO    TT      /PPPPP  PPPPP  PYY  YYYY  YYYYY\  
RR   RR OO    OO BB   BB OO    OO    TT     /PPPPPP  PPPPP  PYY  YYYY  YYYYYY\ 
RR   R  OO    OO BB   B  OO    OO    TT    /PPPPPPP  PPPP   PYYY  YY  YYYYYYYY\
RRRRRR  OO    OO BBBBBB  OO    OO    TT    \PPPPPPP       PPPYYYY    YYYYYYYYY/
RR   RR OO    OO BB   BB OO    OO    TT     \PPPPPP  PPPPPPPPYYYYY  YYYYYYYYY/ 
RR   RR OO    OO BB   BB OO    OO    TT      \PPPPP  PPPPPPPPYYYYY  YYYYYYYY/  
RR   RR OO    OO BB   BB OO    OO    TT       \PPPP  PPPPPPPPYYYYY  YYYYYYY/   
RR   RR  OOOOOO  BBBBBB   OOOOOO     TT        \PPP  PPPPPPPPYYYYY  YYYYYY/    
                                                \PPPPPPPPPPPPYYYYYYYYYYYY/     
                                                 \PPPPPPPPPPPYYYYYYYYYYY/      
                                                  \PPPPPPPPPPYYYYYYYYYY/       
"""

    try:
        from colorama import init, Back, Style

        init()
        robotpy_logo = (
            robotpy_logo.replace("R", Back.BLUE + "R" + Style.RESET_ALL)
            .replace("O", Back.BLUE + "O" + Style.RESET_ALL)
            .replace("B", Back.BLUE + "B" + Style.RESET_ALL)
            .replace("T", Back.BLUE + "T" + Style.RESET_ALL)
            .replace("P", Back.BLUE + "P" + Style.RESET_ALL)
            .replace("Y", Back.BLUE + "Y" + Style.RESET_ALL)
            + Style.RESET_ALL
        )
    except:
        pass

    print(robotpy_logo)


if __name__ == "__main__":
    main()
