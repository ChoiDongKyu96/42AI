# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dochoi </var/mail/dochoi>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/14 06:09:40 by dochoi            #+#    #+#              #
#    Updated: 2020/04/14 06:09:44 by dochoi           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from string import punctuation
import sys

dic = {'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
        'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
        'M':'--', 'N':'-.', 'O':'---', 'P':".--.",'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
        'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Y':'-.--', 'Z':'--..',
        " ": "/"}

if __name__ == "__main__":
    i = 1
    len_argv = len(sys.argv)
    if len_argv == 1:
        print("ERROR")
        sys.exit()
    else:
        while i < len_argv:
            s = sys.argv[i].replace(" ", "")
            if not s.isalnum():
                print("ERROR")
                sys.exit()
            i += 1
    text = " ".join(sys.argv[1::])
    text = text.upper()
    for c in text:
        print(dic[c], end=' ')
    print("")
