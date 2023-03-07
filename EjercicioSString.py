name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'
template="""Gravity Facts Abaut{name}
Planet: {planet}
gravity on {name}: {gravity} m/s"""
print(template.format(name=name, planet=planet, gravity=gravity))