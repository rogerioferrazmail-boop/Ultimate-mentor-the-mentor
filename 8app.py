from ics import Calendar, Event

def gerar_ics(sessao, nome):
    c = Calendar()
    e = Event()
    e.name = f"Sessão com {sessao['mentor']}"
    e.begin = f"{sessao['data']} 18:00"
    e.duration = {"minutes": 60}
    e.description = f"Link Zoom: {sessao['zoom']}"
    e.location = "Online"
    c.events.add(e)
    with open(f"{nome}_sessao.ics", "w") as f:
        f.writelines(c)