from django.shortcuts import render

def shades_view(request):
    shades = []

    # We want 50 steps. To go from 0 to 255 evenly over 50 steps,
    # we divide 255 by 49 (since index goes from 0 to 49).
    step = 255 / 49

    for i in range(50):
        val = int(i * step)

        # Build a dictionary for each row containing the exact CSS rgb() string
        shades.append({
            'noir': f'rgb({val}, {val}, {val})',
            'rouge': f'rgb({val}, 0, 0)',
            'bleu': f'rgb(0, 0, {val})',
            'vert': f'rgb(0, {val}, 0)'
        })

    return render(request, 'ex03/index.html', {'shades': shades})
    # We want 50 steps. To go from 0 to 255 evenly over 50 steps,
    # we divide 255 by 49 (since index goes from 0 to 49).
