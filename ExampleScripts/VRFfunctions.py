__author__ = 'claytonmiller'

#Defines the Function for two dimensional Biquadratic
def TwoDimBiquadratic(A,B,p):
    return(p[0] + p[1]*A + p[2]*A**2 + p[3]*B + p[4]*B**2 + p[5]*A*B)

#Defines the Function for 1 Dimensional Linear
def OneDimensionLinear(A,p):
    return (p[0] + p[1]*A)

#Defines the Function for 1 Dimensional Quadratic
def OneDimensionQuadratic(A,p):
    return (p[0] + p[1]*A + p[2]*A**2)

#Defines the Function for 1 Dimensional Cubic 
def OneDimensionCubic(A,p):
    return (p[0] + p[1]*A + p[2]*A**2 + p[3]*A**3)

#Defines residuals used in BiQuadratic
def residualsTwoDimBiquadratic(p,I,A,B):
    err = (I - TwoDimBiquadratic(A,B,p))
    return err

#Defines residuals used in Linear, 1 dimensional eq
def residualsOneDimLinear(p,I,A):
    err = (I - OneDimensionLinear(A,p))
    return err

#Defines residuals used in Quadratic, 1 dimensional eq
def residualsOneDimQuadratic(p,I,A):
    err = (I - OneDimensionQuadratic(A,p))
    return err

#Defines residuals used in Cubic, 1 dimensional eq
def residualsOneDimCubic(p,I,A):
    err = (I - OneDimensionCubic(A,p))
    return err