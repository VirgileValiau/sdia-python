import numpy as np

from lab2.utils import get_random_number_generator


class BoxWindow:
    """BoxWindow is an object of N dimension. In 1D, it can be represented by a range, in 2D a rectangle and in 3D a box"""

    def __init__(self, bounds):
        """This method initializes the box, thanks to the ranges of the box in parameter.

        bounds:
            bounds (list): list of ranges of the box in all the directions of the space.
        """
        # * consider np.array(bounds) to exploit numpy vectorization power
        self.bounds = bounds

    def __str__(self):
        r"""BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            [string]: Writing expression of the box with its bounds.
        """
        S = "BoxWindow: "  # * convention/naming use lower case s or string
        # * consider for i, (a, b) in enumerate(self.bounds)
        for i in range(len(self.bounds)):  # ! iterate over self.bounds
            S += "[" + str(self.bounds[i][0]) + ", " + str(self.bounds[i][1]) + "]"
            if i != len(self.bounds) - 1:
                S += " x "
        return S

    def __len__(self):
        # ! len/dimension is not tested
        """Returns the number of dimension of the box"""
        return len(self.bounds)

    def __contains__(self, point):
        """Returns true if a point is contained in the box. The coordinates of the point are given in parameter.

        args:
            args (array): list of coordinates of the point
        """
        # * consider for (a, b), x in zip(self.bounds, point)
        for i, x in enumerate(point):
            print(self.bounds[i][0], x, self.bounds[i][1])
            if not (self.bounds[i][0] <= x <= self.bounds[i][1]):
                return False
        return True

    def dimension(self):
        # ! len/dimension is not tested
        """Returns the number of dimension of the box"""
        # ? what does "number of dimension" mean
        return len(self)

    def volume(self):
        """Returns the volume of the box"""
        # * exploit numpy vectors, use - or np.diff, and np.prod
        res = 1
        for i in range(len(self.bounds)):
            longueur = np.sqrt((self.bounds[i][1] - self.bounds[i][0]) ** 2)
            res = res * longueur
        return res

    def indicator_function(self, point):
        """return the image of the point through the indicator function described by the bow window

        Args:
            args ([type]): [description]
        """
        # ? how would you handle multiple points
        # todo readability consider using "point in self"
        return self.__contains__(point)

    def rand(self, n=1, seed=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): Number of points. Defaults to 1.
            rng ([type], optional): generator of a random number. Defaults to None.
        """
        rng = get_random_number_generator(seed)
        # * exploit numpy, rng.uniform(a, b, size=n)
        L = []  # * naming: use a more explicit name
        for i in range(n):  # ! iterate over self.bounds
            # * convention: use _ for unused counters
            Point = []  # * convention: variables are lower cased
            for j in range(self.dimension()):
                Point.append(rng.uniform(self.bounds[j][0], self.bounds[j][1]))
            L.append(Point)
        return L

    def center(self):
        """Returns the coordinates of the center of the box"""
        # * exploit numpy vectors, use - or np.diff, and +
        # * same remarks as in rand function
        l = []
        for i in range(len(self.bounds)):
            l.append(round((self.bounds[i][0] + self.bounds[i][1]) / 2, 2))
        print(l)
        return np.array(l)


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """Create a Box window with bounds of length equal to 1
        # ? what is the default UnitBoxWindow
        # todo consider passing default arguments
        # todo complete the docstring

        Args:
            dimension (int): dimension de la boite
            center (np.array): centre de la boite.
        """
        assert len(center) == dimension
        bounds = np.zeros((dimension, 2))
        for i in range(dimension):
            bounds[i] = [center[i] - 0.5, center[i] + 0.5]

        # ! use super(UnitBoxwindow, self).__init__(bounds)
        BoxWindow.__init__(self, bounds)
