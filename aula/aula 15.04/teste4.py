import panel as pn
 
pn.extension(template='material')
 
number = pn.widgets.IntSlider(value=3, start=0, end=10, name='number')
size = pn.widgets.IntSlider(value=10, start=10, end=25, step=5, name='size')


pn.Column(
    number, size,
    pn.pane.Markdown(
        pn.bind(lambda n: "⭐" * n, number),
        styles=pn.bind(lambda size: {'font-size': f'{size}px'}, size)
    )
).servable(title='Our Simple App')