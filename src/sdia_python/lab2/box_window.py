import numpy as np

from sdia_python.lab2.utils import get_random_number_generator


class BoxWindow:
    """BoxWindow is an object of N dimension. In 1D, it can be represented by a range, in 2D a rectangle and in 3D a box"""

    def __init__(self, bounds):
        """This method initializes the box, thanks to the ranges of the box in parameter.

        bounds:
            bounds (list): list of ranges of the box in all the directions of the space.
        """
        # * consider np.array(bounds) to exploit numpy vectorization power
        self.bounds = np.array(bounds)

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [string]: Writing expression of the box with its bounds.
        """
        S = "BoxWindow: "  # * convention/naming use lower case s or string
        # * consider for i, (a, b) in enumerate(self.bounds)
        S += "[" + str(self.bounds[0][0]) + ", " + str(self.bounds[0][1]) + "]"
        for b in self.bounds[1:]:
            S += " x "
            S += "[" + str(b[0]) + ", " + str(b[1]) + "]"
        return S

    def __len__(self):
        """Returns the number of dimension of the box"""
        return len(self.bounds)

    def __contains__(self, point):
        """Returns true if a point is contained in the box. The coordinates of the point are given in parameter.

        args:
            args (array): list of coordinates of the point
        """
        # * consider for (a, b), x in zip(self.bounds, point)
        for (a, b), x in zip(self.bounds, point):
            if not (a <= x <= b):
                return False
        return True

    def dimension(self):
        """Returns the dimension of the box"""
        return len(self)

    def volume(self):
        """Returns the volume of the box"""
        Tmp = self.bounds[:, 1] - self.bounds[:, 0]
        return np.prod(Tmp)

    def indicator_function(self, point):
        """return the image of the point through the indicator function described by the bow window

        Args:
            args (Array): point we pass through the indicator function
        """
        return point in self

    def rand(self, n=1, seed=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): Number of points. Defaults to 1.
            rng ([type], optional): generator of a random number. Defaults to None.
        """

        ## This function is tested with the Pi Approximation exercise in lab3.pynb

        rng = get_random_number_generator(seed)
        RandListe = []
        for (a, b) in self.bounds:
            point = rng.uniform(a, b, size=n)
            RandListe.append(point)
        return np.array(RandListe).T

    def center(self):
        """Returns the coordinates of the center of the box"""
        return np.round(0.5 * (self.bounds[:, 0] + self.bounds[:, 1]), 2)


class UnitBoxWindow(BoxWindow):
    def __init__(self, center=np.array([0, 0]), dimension=2):
        """Generate a Unit Window with unit size lenght

        Args:
            center (Array, optional): Define the center of the unit box. Defaults to np.array([0, 0]).
            dimension (int, optional): Define the dimension of the unit box. Defaults to 2.
        """
        assert len(center) == dimension
        bounds = np.zeros((dimension, 2))
        for i in range(dimension):
            bounds[i] = [center[i] - 0.5, center[i] + 0.5]

        # ! use super(UnitBoxwindow, self).__init__(bounds)
        # ! Doesn't work for us   :((((
        # This works :
        BoxWindow.__init__(self, bounds)
