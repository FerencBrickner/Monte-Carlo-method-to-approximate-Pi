import logging
from random import uniform
from typing import Callable, Generator


def approximate_pi_via_monte_carlo_method(
    *,
    step_count: int = int(1e10),
    log_interval: int = int(1e6),
    is_point_within_quarter_circle: Callable[[float, float], bool] = lambda x, y: x * x
    + y * y
    < 1,
    number_of_points_within_quarter_circle: int = 0,
) -> Generator[float, None, None]:
    for current_step in range(1, step_count + 1):
        x: float = uniform(0, 1)
        y: float = uniform(0, 1)
        number_of_points_within_quarter_circle += is_point_within_quarter_circle(x, y)
        if current_step % log_interval == 0:
            pi = 4 * number_of_points_within_quarter_circle / current_step
            yield pi


def main(*args, **kwargs) -> None:
    """
    Approximating Pi via the Monte Carlo method.
    Logs periodic approximations of Pi to the console.
    https://en.wikipedia.org/wiki/Monte_Carlo_method
    """
    logging.basicConfig(level=logging.INFO)
    pi_approximations = approximate_pi_via_monte_carlo_method()

    for pi_approximation in pi_approximations:
        logging.info(f"Current Pi approximation: {pi_approximation:.15f}")


if __name__ == "__main__":
    main()
