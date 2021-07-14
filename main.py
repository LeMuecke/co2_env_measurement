from screens import Screen, Page_CO2Main
from tasks import CO2ReaderTask, TemperatureReaderTask, HumidityReaderTask, TemperatureHumiditySensor, PlotBuilderTask, \
    PingReaderTask, GestureReaderTask

if __name__ == '__main__':
    screen = Screen()

    temp_hum_sensor = TemperatureHumiditySensor()
    tasks = {
        "co2": CO2ReaderTask(deque_max_length=2500, sleep_time=8),
        "temperature": TemperatureReaderTask(deque_max_length=2500, temp_hum_sensor=temp_hum_sensor, sleep_time=5),
        "humidity": HumidityReaderTask(deque_max_length=2500, temp_hum_sensor=temp_hum_sensor, sleep_time=5),
        "ping": PingReaderTask(deque_max_length=0),
        "gesture": GestureReaderTask(deque_max_length=0, screen=screen)
    }
    tasks["plot"] = PlotBuilderTask(deque_max_length=0, co2_reader_task=tasks["co2"], screen=screen)

    page_co2_main = Page_CO2Main(screen=screen, tasks=tasks)
    screen.add_pages([page_co2_main])

    screen.main_loop()
