import turtle
import figures
import time

# --- AGRESYWNY RESET ---
# Próbujemy zamknąć stare okno siłowo, żeby proces nie wisiał
try:
    turtle.bye()
except Exception:
    pass # Jeśli okna nie było, to dobrze

# Dajemy chwilę na zamknięcie procesu w tle
time.sleep(0.5)

# --- INICJALIZACJA ---
# Tworzymy ekran od nowa
try:
    window = turtle.Screen()
    window.title("Rysowanie figur - nowa sesja")
    window.setup(width=800, height=600)
    window.bgcolor("lightgreen")
    
    # Czyścimy wszystko
    window.clearscreen()
except turtle.Terminator:
    # Ostatnia deska ratunku - jeśli Screen() rzuci błąd, tworzymy go jeszcze raz
    window = turtle.Screen()
    window.clearscreen()

# Ustawienia żółwia
turtle.speed(5)
turtle.shape("turtle")

# --- RYSOWANIE ---

print("Rysuję pierwszy kwadrat...")
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
figures.draw_square(100)

print("Rysuję drugi kwadrat...")
# Dodajemy małe opóźnienie dla stabilności
time.sleep(0.2)
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
figures.draw_square(100)


print("Rysuję pierwszy trójkąt...")
time.sleep(0.2)
turtle.penup()
turtle.goto(-200, 50)
turtle.pendown()
figures.draw_triangle(100)

print("Rysuję drugi trójkąt...")
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
figures.draw_triangle(100)


print("Rysuję pierwszy prostokąt...")
time.sleep(0.2)
turtle.penup()
turtle.goto(-200, -150)
turtle.pendown()
figures.draw_rectangle(120, 80)

print("Rysuję drugi prostokąt...")
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
figures.draw_rectangle(120, 80)

print("Skończone! Kliknij w okno, aby zamknąć.")

turtle.hideturtle()
window.exitonclick()