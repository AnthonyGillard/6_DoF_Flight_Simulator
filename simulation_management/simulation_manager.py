import time as sys_time


class Simulation:
    version = "v0.0.1"
    OUTPUT_WIDTH = 120

    _end_information_block = '/' + '-' * (OUTPUT_WIDTH - 2) + '\\' + '\n'
    _welcome_text = '/' + f'Welcome to Flight Simulator {version}'.center(OUTPUT_WIDTH - 2) + '\\\n'
    _simulation_entities_text = '\n/' + f'Simulation Entities'.center(OUTPUT_WIDTH - 2) + '\\\n'
    _simulation_starting_text = '/' + f'Simulation Started'.center(OUTPUT_WIDTH - 2) + '\\'
    _simulation_ended_text = '\n/' + f'Simulation Ended'.center(OUTPUT_WIDTH - 2) + '\\\n'

    def __init__(self):
        self.running = False

    def start_simulation(self):
        self._print_introduction()
        self._print_entities_description()

        print(self._simulation_starting_text)

        iteration = 0
        time = 0
        self.running = True
        while self.running:
            if iteration % 10 == 0:
                if iteration == 0:
                    print(f'Time:' + f'{time:.2f}s'.rjust(8), end='')
                else:
                    print(f'\nTime:' + f'{time:.2f}s'.rjust(8), end='')
            else:
                print(".", end='')
            time += 0.1
            iteration += 1

            sys_time.sleep(0.1)

            if time >= 10:
                self.running = False

        print(self._simulation_ended_text)

    def _print_introduction(self):
        print(self._end_information_block + self._welcome_text + self._end_information_block)

    def _print_entities_description(self):
        print(self._simulation_entities_text)


if __name__ == "__main__":
    simulation = Simulation()
    simulation.start_simulation()