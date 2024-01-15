import flet as ft
import time
from flet_core import TemplateRoute

def main(page: ft.Page):

    

    # añadir o actualizar controles de la pagina
    t = ft.Text()
    page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(1):
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)
    pass


    # añadir elementos al row 
    # page.add(
    #     ft.Row(controls=[
    #         ft.Text("A"),
    #         ft.Text("B"),
    #         ft.Text("C")
    #     ])
    # )


    # for i in range(10):
    #     page.controls.append(ft.Text(f"Line {i}"))
    #     if i > 4:
    #         page.controls.pop(0)
    #     page.update()
    #     time.sleep(0.3)

    # def button_clicked(e):
    #     page.add(ft.Text("Clicked!"))

    # page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))


    # def add_clicked(e):
    #     page.add(ft.Checkbox(label=new_task.value))
    #     new_task.value = ""
    #     new_task.focus()
    #     new_task.update()

    # new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    # page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    # first_name = ft.TextField()
    # last_name = ft.TextField()
    # first_name.disabled = True
    # last_name.disabled = True
    # page.add(first_name, last_name)

    # añadir elementos por columnas
    # first_name = ft.TextField(hint_text="fist_name")
    # last_name = ft.TextField(hint_text="fist_name")
    # c = ft.Column(controls=[
    #     first_name,
    #     last_name
    # ])
    # # c.disabled = True
    # page.add(c)

    # first_name = ft.TextField(label="First name", autofocus=True)
    # last_name = ft.TextField(label="Last name")
    # greetings = ft.Column()

    # def btn_click(e):
    #     greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
    #     first_name.value = ""
    #     last_name.value = ""
    #     page.update()
    #     first_name.focus()

    # page.add(
    #     first_name,
    #     last_name,
    #     ft.ElevatedButton("Say hello!", on_click=btn_click),
    #     greetings,
    # )

    # gv = ft.GridView(expand=True, max_extent=100, child_aspect_ratio=1)
    # page.add(gv)

    # for i in range(5000):
    #     gv.controls.append(
    #         ft.Container(
    #             ft.Text(f"Item {i}"),
    #             alignment=ft.alignment.center,
    #             bgcolor=ft.colors.AMBER_100,
    #             border=ft.border.all(1, ft.colors.AMBER_400),
    #             border_radius=ft.border_radius.all(5),
    #         )
    #     )
    # page.update()

    # import flet as ft


    # add ListView to a page first
    # lv = ft.ListView(expand=1, spacing=10, item_extent=50)
    # page.add(lv)

    # for i in range(5100):
    #     lv.controls.append(ft.Text(f"Line {i}"))
    #     # send page to a page
    #     if i % 500 == 0:
    #         page.update()
    # # send the rest to a page
    # page.update()


    # page.title = "Drag and Drop example"

    # def drag_accept(e):
    #     # get draggable (source) control by its ID
    #     src = page.get_control(e.src_id)
    #     # update text inside draggable control
    #     src.content.content.value = "0"
    #     # update text inside drag target control
    #     e.control.content.content.value = "1"
    #     page.update()

    # page.add(
    #     ft.Row(
    #         [
    #             ft.Draggable(
    #                 group="number",
    #                 content=ft.Container(
    #                     width=50,
    #                     height=50,
    #                     bgcolor=ft.colors.CYAN_200,
    #                     border_radius=5,
    #                     content=ft.Text("1", size=20),
    #                     alignment=ft.alignment.center,
    #                 ),
    #             ),
    #             ft.Container(width=100),
    #             ft.DragTarget(
    #                 group="number",
    #                 content=ft.Container(
    #                     width=50,
    #                     height=50,
    #                     bgcolor=ft.colors.PINK_200,
    #                     border_radius=5,
    #                     content=ft.Text("0", size=20),
    #                     alignment=ft.alignment.center,
    #                 ),
    #                 on_accept=drag_accept,
    #             ),
    #         ]
    #     )
    # )

    # troute = TemplateRoute(page.route)

    # if troute.match("/books/:id"):
    #     print("Book view ID:", troute.id)
    # elif troute.match("/account/:account_id/orders/:order_id"):
    #     print("Account:", troute.account_id, "Order:", troute.order_id)
    # else:
    #     print("Unknown route")


ft.app(target=main)