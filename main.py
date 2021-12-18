from flask import Flask, request

app = Flask(__name__)

home = '''
Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max 10 próbach:

<br><br>
<form action='/' method='POST'>
<input type="hidden" name="min" value="{}">
<input type="hidden" name="max" value="{}">    
<label><button type="submit" name="submit_button" value="Start">Start</button></label>
</form>
'''

form = '''Zgaduję: {guess}
    <form action='/' method='POST'>
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">    
    <input type="hidden" name="guess" value="{guess}">    
    <label><button type="submit" name="submit_button" value="Too big">Too big</button></label>
    <label><button type="submit" name="submit_button" value="Too small">Too small</button></label>
    <label><button type="submit" name="submit_button" value="You win">You win</button></label>
    </form>'''

win = 'Wygrałeś'

@app.route('/', methods=['GET', 'POST'])
def zgadywanie():
    if request.method == 'GET':
        return home.format(0 ,1000)
    else:
        min = int(request.form.get('min'))
        max = int(request.form.get('max'))
        guess = int(request.form.get('guess', 500))
        answer = request.form.get('submit_button')

        if answer == 'Too big':
            max = guess
        elif answer == 'Too small':
            min = guess
        elif answer == 'You win':
            return win

        guess = (max - min) // 2 + min

        return form.format(guess=guess, min=min, max=max)


if __name__ == '__main__':
    app.run(debug=True)