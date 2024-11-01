def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        "manufacturer": manufacturer.title(),
        "model": model.title(),
    }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict


car1 = make_car("subaru", "outback", color="blue", tow_package=True, heated_seat=True)
print(car1)

car2 = make_car(
    "honda",
    "accord",
    year=1991,
    color="white",
    headlights="popup",
    twin_cam=True,
    steering_wheel_color="red",
)
print(car2)
