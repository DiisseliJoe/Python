ULKONA = -1
NURKASSA = 0
LAIDALLA = 1
KESKELLA = 2

TULOSTUKSET = {
    ULKONA: "Antamasi ruutu on kentän ulkopuolella.",
    NURKASSA: "Antamasi ruutu on kentän nurkassa",
    LAIDALLA: "Antamasi ruutu on kentän laidassa",
    KESKELLA: "Antamasi ruutu on kentän keskellä"
}

def sijainti_kentalla(x_koor,y_koor,korkeus,leveys):
    #tarkastaa onko joku koordinaatti arvo ulkona jos on palauttaa -1
    if x_koor > leveys or x_koor < 0 or y_koor > korkeus or y_koor < 0:
        tulosta_sijainti(ULKONA)
        return
    #jos x on reunassa tarkastaa onko y myös reunassa jos y on reunassa koordinaatti on kulmassa ja jos ei niin koordinaatti on sivu laidalla
    if x_koor == 0 or x_koor == leveys:
        if y_koor == 0 or y_koor == korkeus:
            tulosta_sijainti(NURKASSA)
        else:
            tulosta_sijainti(LAIDALLA)
        return
    #jos y on reunassa tarkastaa onko x myös reunassa jos x on reunassa koordinaatti on kulmassa ja jos ei niin koordinaatti on ylä tai ala laidalla
    if y_koor == 0 or y_koor == korkeus:
        if x_koor == 0 or x_koor == leveys:
            tulosta_sijainti(NURKASSA)
        else:
            tulosta_sijainti(LAIDALLA)
        return
    #jos aiemmat eivät osuneet niin piste on kentän keskellä
    else:
        tulosta_sijainti(KESKELLA)

#functiota kutsutaan ylemmästä antaen paikka arvo jonka avulla tulostaa kirjastosta oikean tekstin
def tulosta_sijainti(arvo):
    print(TULOSTUKSET.get(arvo))


leveys = int(input("Anna kentän leveys: "))
korkeus = int(input("Anna kentän korkeus: "))  
if leveys <= 0 or korkeus <= 0:
    print("Noin pienelle kentälle ei mahdu ainuttakaan ruutua")
else:
    x_koordinaatti = int(input("Anna x-koordinaatti: "))
    y_koordinaatti = int(input("Anna y-koordinaatti: "))
    sijainti_kentalla(x_koordinaatti,y_koordinaatti,korkeus,leveys)