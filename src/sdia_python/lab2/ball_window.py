import numpy as np

from sdia_python.lab2.utils import get_random_number_generator


class BallWindow:
    """BallWindow is an object of N dimension. In 1D, it can be represented by a range, in 2D a circle and in 3D a ball, for dimensions higher, it's hard to represent the ball.
    """

    def __init__(self, centre, radius):
        """This method initializes the ball, thanks to the center of the ball and its radius.

        Args:
            centre (array): center of the ball
            radius (int): radius of the ball
        """

        self.radius = radius
        self.centre = centre

    def __str__(self):
        """print the center and the radius of the ball
        """

        return f"BallWindow with center: {self.centre[0]} and radius: {self.radius}"

    def __len__(self):
        """Returns the number of dimension of the ball"""
        return len(self.centre)

    def __contains__(self, point):
        """Returns true if a point is contained in the ball. The coordinates of the point are given in parameter.

        Args:
            point (array): array of coordinates of the point
        """
        dist = (point - self.centre) ** 2
        dist = np.sqrt(np.sum(dist))
        return dist <= self.radius

    def dimension(self):
        """Returns the dimension of the ball"""
        return len(self)

    def volume(self):
        """volume/area/length of the BallWindow, we can't calculate for higher dimensions because we don't know the formula


        Returns:
            int: volume/area/length
        """

        assert len(self) <= 3
        if len(self) == 3:
            return (4 * np.pi * self.radius ** 3) / 3
        if len(self) == 2:
            return np.pi * self.radius ** 2
        return 2 * self.radius

    def indicator_function(self, point):
        """return the image of the point through the indicator function described by the ball window

        Args:
            args (array): points to test
        """
        return point in self

    def rand_2d(self, n=1, seed=None):
        """generate n random points in a 2d ball window

        Args:
            n (int): number of points to generate
            seed (int): describe the generator. Defaults to None.
        """

        rng = get_random_number_generator(seed)
        rad = np.sqrt(rng.uniform(0, self.radius ** 2, size=n))
        theta = rng.uniform(0, 2 * np.pi, size=n)
        Points = np.zeros((n, 2))
        Points[:, 0] = rad * np.cos(theta)
        Points[:, 1] = rad * np.sin(theta)
        return Points
