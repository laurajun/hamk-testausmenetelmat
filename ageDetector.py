def agerange(age):

    if not type(age) is int:
       result = "Virheellinen syöte"
       return result
    
    if age < 0:
        result = "Ikä ei voi olla negatiivinen luku"
        return result
    
    if age > 120:
        result = "Mahdatko olla noin iäkäs?"
        return result
    
    if age < 18:
        result = "Olet lapsi"
        return result
    
    elif age >= 18 and age <= 70:
        result = "Olet aikuinen"
        return result
    
    else:
        result = "Olet eläkeläinen"
        return result
        
