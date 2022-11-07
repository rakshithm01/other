#plotting the imaginary part of the dielectric function obtained from the lorentz model
import numpy as np
import matplotlib.pyplot as plt

def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)


x = np.linspace(0,4, 1000)

w0=2
b= [0.08, 0.2, 0.5]
e1 = []
e2 = []
e3 = []
for i in x:
	e1.append(b[0]*i/((w0**2-i**2)**2+b[0]**2 * i**2))
	e2.append(b[1]*i/((w0**2-i**2)**2+b[1]**2 * i**2))
	e3.append(b[2]*i/((w0**2-i**2)**2+b[2]**2 * i**2))
plt.style.use('bmh')
plt.plot(x, e1)
plt.plot(x, e2, c='tab:orange')
plt.plot(x, e3, c='g')
plt.xlabel('Frequency (\u03C9)')
plt.ylabel('Imaginary part of dielectric function (\u03B5)'+get_sub('imag'))
plt.legend(['\u03B2 = 0.08', '\u03B2 = 0.2', '\u03B2 = 0.5'])
plt.savefig('filename.png', dpi=600, bbox_inches="tight")
plt.show()
	
