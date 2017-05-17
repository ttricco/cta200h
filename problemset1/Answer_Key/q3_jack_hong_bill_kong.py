# CTA200H 2017 Problem Set 1, Question 3
# Jack Hong and Bill Kong

import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from astropy.convolution import AiryDisk2DKernel
from astropy.convolution import convolve


def bessel(m, x):
    """Return the Bessel function of the first kind of order m."""
    return 1 / np.pi * float(integrate.quad(lambda theta: np.cos(m * theta - x * np.sin(theta)), 0, np.pi)[0])


def plot_bessel(m_max, x_max):
    """Plot the bessel functions of the first kind from order m=0 to m=m_max for x=[0, xmax]"""
    x = np.linspace(0, x_max, 1000)
    vec_bessel = np.vectorize(bessel)

    for m in range(m_max + 1):
        plt.plot(x, vec_bessel(m, x), label='m = {:d}'.format(m))

    plt.title("Bessel functions of the first kind of order m")
    plt.ylabel("$J_m(x)$")
    plt.xlabel("x")
    plt.legend()


def point_spread_intensity(q):
    """Return the point spread function.
    
    The point_spread_intensity of light from a point source passing through a circular telescope aperture
    of radius a on the focal plane is modelled by the point spread function:
        I(x) = Io (2*J1(x)/x)^2
    where Io is the initial point_spread_intensity and x = (2 * pi * a * q) / (w * R)
    
    a - the radius of the aperture
    q - distance from the optical axis in the focal plane
    w - wavelength of the light
    R - distance from aperture to the focal plane.
    
    The values for the above parameters are arbitrarily chosen for the assignment
    and not intended to represent a real thing.
    """
    I_0 = 1000  # Intensity of light at center
    a = 0.1  # aperture of telescope
    w = 0.07  # wavelength of light
    R = 0.5  # distance from aperture to focal point
    x = (2 * np.pi * a * q) / (w * R)

    return I_0 * (2 * bessel(1, x) / x) ** 2


def plot_point_spread_fn():
    """Plot the point spread function.
    
    Note: The contrast has been increased by taking the log of the point_spread_intensity function and specifying vmax=7
    """
    # q = np.linspace(1e-6, 1, 100)
    # vec_intensity = np.vectorize(point_spread_intensity)
    # plt.plot(q, vec_intensity(q))
    # plt.show()

    x = np.linspace(-0.5, 0.5, 100)
    vec_intensity = np.vectorize(point_spread_intensity)
    xv, yv = np.meshgrid(x, x)
    r2d = np.sqrt(xv ** 2 + yv ** 2)
    intensities = vec_intensity(r2d)
    plt.imshow(np.log(intensities), extent=(-.5, .5, -.5, .5), cmap='Greys', vmin=0, vmax=7)
    plt.title("2D Point spread function (Airy disk)")
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')


def convolute_img():
    img = mpimg.imread('comet.png')
    img = img.mean(axis=-1)

    plt.subplot(2, 1, 1)
    plt.imshow(img)
    plt.title("Original")

    plt.subplot(2, 1, 2)
    # len = img.shape[0]
    # height = img.shape[1]
    # x = np.linspace(-0.5, 0.5, len)
    # y = np.linspace(-0.5, 0.5, height)
    # xv, yv = np.meshgrid(x, y)
    # r2d = np.sqrt(xv**2 + yv**2)
    #
    # vec_intensity = np.vectorize(point_spread_intensity)
    # intensities = vec_intensity(r2d)

    airydisk_2D_kernel = AiryDisk2DKernel(10)

    convolved_img = convolve(img, airydisk_2D_kernel)
    plt.imshow(convolved_img)
    plt.title("Convoluted")


def main():
    plt.figure()
    plot_bessel(3, 20)

    plt.figure()
    plot_point_spread_fn()

    plt.figure()
    convolute_img()

    plt.show()


if __name__ == "__main__":
    main()
