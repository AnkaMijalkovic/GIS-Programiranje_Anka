# Zadatak 7 (Vezba 2)

import random
from random import randint

print 'Ovo je igra Ajnc!'
ime = raw_input('Unesite svoje ime:')


def spil():
    vrednost_karte = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
    tip_karte = ['Srce', 'Pik', 'Tref', 'Karo']
    deck = []
    for i in tip_karte:
        for j in vrednost_karte:
            deck.append(j + ' ' + i)
    return deck


def vrednost_karte(card):
    if card[:1] in ('J','Q','K','1'):
        return int(10)
    elif card[:1] in ('2', '3', '4', '5', '6', '7', '8', '9'):
        return int(card[:1])
    elif card[:1] == 'A':
        print ("\n" + str(card))
        num = input("Da li zelite da bude 1 ili 11?\n>")
        while num != '1' or num != '11':
            if num == '1':
                return int(1)
            elif num == '11':
                return int(11)
            else:
                num = input("Da li zelite da bude 1 ili 11?\n>")


def nova_karta(deck):
    return deck[randint(0, len(deck) - 1)]


def remove_card(deck, card):
    return deck.remove(card)


igraj_ponovo = ''
while igraj_ponovo != 'EXIT':
    # deck creation, card creation, card removal from deck, values and ukupnos
    new_deck = spil()
    karta1 = nova_karta(new_deck)
    remove_card(new_deck, karta1)
    karta2 = nova_karta(new_deck)
    remove_card(new_deck, karta2)
    print (
    "\n\n\n" + "Vase karte su: " + karta1 + " i " + karta2)  # doing this statement first allows for selection between 1 and 11
    vrednost1 = vrednost_karte(karta1)
    vrednost2 = vrednost_karte(karta2)
    ukupno_igrac = vrednost1 + vrednost2
    print("Ukupno imate " + str(ukupno_igrac) + " poena.")

    # dealer's hand
    dealer_karta1 = nova_karta(new_deck)
    remove_card(new_deck, dealer_karta1)
    dealer_karta2 = nova_karta(new_deck)
    remove_card(new_deck, dealer_karta2)
    dealer_value1 = vrednost_karte(dealer_karta1)
    dealer_value2 = vrednost_karte(dealer_karta2)
    dealer_ukupno = dealer_value1 + dealer_value2
    print ("\n Dilerova prva karta je " + dealer_karta1 + " i karta okrenuta licem dole.")

    if ukupno_igrac == 21:
        print("Blackjack!")
    else:
        while ukupno_igrac < 21:  # not win or loss yet
            odgovor = input("Da li zelite 'hit' (dobijate novu kartu) ili 'stand' (ne dobijate kartu)?\n> ")
            if odgovor.lower() == 'hit':
                # more card creation, removal, and value added to ukupno
                jos_karata = nova_karta(new_deck)
                remove_card(new_deck, jos_karata)
                jos_vrednost = vrednost_karte(jos_karata)
                ukupno_igrac += int(jos_vrednost)
                print ("Nova karta je: " + jos_karata + ", novi Vas zbir je " + str(ukupno_igrac))
                if ukupno_igrac > 21:  # lose condition
                    print("IZGUBILI STE!")
                    igraj_ponovo = input("Ako zelite da nastavite unesite 'continue', ako ne unesite 'EXIT'\n")
                elif ukupno_igrac == 21:  # winning condition
                    print("POBEDILI STE")
                    igraj_ponovo = input("Ako zelite da nastavite unesite 'continue', ako ne unesite 'EXIT'\n")
                else:
                    continue
            elif odgovor.lower() == 'stand':
                print("Diler otkriva svoju drugu kartu ")
                print(dealer_karta2 + " i ukupno ima " + str(dealer_ukupno))
                if dealer_ukupno < 17:
                    print("Diler 'hits' ponovo.")
                    dealer_more = nova_karta(new_deck)
                    more_dealer_value = vrednost_karte(dealer_more)
                    print("Karta je  " + str(dealer_more))
                    dealer_ukupno += int(more_dealer_value)
                    if dealer_ukupno > 21 and ukupno_igrac <= 21:
                        print("POBEDILI STE!")
                    elif dealer_ukupno < 21 and dealer_ukupno > ukupno_igrac:
                        print("Diler ima " + str(dealer_ukupno) + " IZGUBILI STE!")
                    else:
                        continue
                elif dealer_ukupno == ukupno_igrac:
                    print("Nema pobednika")
                elif dealer_ukupno < ukupno_igrac:
                    print("POBEDILI STE!")
                else:
                    print("IZGUBILI STE!")
                igraj_ponovo = input("\nAko zelite da nastavite unesite 'continue', ako ne unesite 'EXIT'\n")
                break
print("Hvala sto ste igrali!")
