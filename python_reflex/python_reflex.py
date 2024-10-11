import reflex as rx #Es la manera de importar el codigo

def index() -> rx.Component:
    return rx.box (

    )

app = rx.App(

)
app.add_page(
    index,
    title="Mi página con Python",
    description="Esto va ser un dolor de huevo",
)

app._compile()