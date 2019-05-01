import numpy as np
import matplotlib.pyplot as plt

class InterpolatingFunction(object):
    def __init__(self):
        print('initializing Blasius solver class')
        plt.rcParams["figure.figsize"] = [20, 7]
        
    def calculateNodes(self,nNodes,plot=False):
        """Calculates Chebyshev points of the second kind (aka Gauss-Lobatto grid points)

        Parameters:
        nNodes (int): number of grid points

        Returns:
        ndarray: array containing all grind points
        """
        j = np.arange(nNodes)
        nodes = -np.cos(j*np.pi/(nNodes-1))
        
        if plot:
            plt.grid(True)
            plt.plot(nodes,np.zeros(nNodes),'x')
            plt.show()
        
        return(nodes)
    
    def calculateWeights(self,nodes,plot=False):
        """Calculates according weights for barycentric interpolation if provided
        nodes are Chebyshev points of second kind 

        Parameters:
        nodes (ndarray): nodes

        Returns:
        ndarray: weights
        """
        
        weights = np.ones(len(nodes))*np.power((-1),np.arange(len(nodes)))
        weights[0]/=2
        weights[-1]/=2
        
        if plot:
            plt.grid(True)
            plt.plot(nodes,weights,'x')
            plt.show()
        
        return(weights)
    
    def calculateBasisFunctions(self,nodes,weights,n,plot=False):
        """Calculates the basis functions l_j(s) for n equidistant points s
        
        Parameters:
        nodes (ndarray[nNodes]): Gaus-Lobatto nodes
        weights (ndarray[nNodes]): barycentric weights for Gaus-Lobatto nodes

        Returns:
        ndarray[nNodes,n] : values of basis functions on n equidistant points s
        """
        l = np.empty((len(nodes),n))
        s = np.linspace(-1,1,n)
        
        # [sum_{k=0}^{n} w_k/(s-s_k)]^-1
        temp2 = 1/np.sum(np.repeat(np.reshape(weights,[len(weights),1]),len(s),axis=1)/
                         (np.repeat(np.reshape(s,[1,len(s)]),len(nodes),axis=0)-
                          np.repeat(np.reshape(nodes,[len(nodes),1]),len(s),axis=1)),axis=0)
        for j in range(len(nodes)):
            # w_j/(s-s_j):
            temp1 = weights[j]/(s-nodes[j])
            l[j,:]=temp1*temp2
            if plot:
                plt.plot(s,l[j,:])
        if plot:
            plt.plot(nodes,np.zeros(len(nodes))+1,'x')
            plt.grid(True)
            #plt.yscale("Log")
            plt.show()
        return l
    
    def interpolateFunction(self,values,basis,plot=False,nodes=None):
        """Calculates a Lagrange interpolation function for given values at the nodes
        with the given basis functions
        
        Parameters:
        values (ndarray[nNodes]): values at sampling points
        basis (ndarray[nNodes,n]): the basis functions as calculatet with
        corresponding functiong

        Returns:
        ndarray[n] : the interpolation function at n equidistant points
        """
        nNodes = len(values)
        nPoints = len(basis[0])
        p = np.sum(np.repeat(np.reshape(values,(nNodes,1)),nPoints,axis=1)*basis,axis=0)
        if plot:
            plt.plot(np.linspace(-1,1,1000),p)
            plt.plot(nodes,values,'x')
            plt.grid(True)
            plt.show()
        return(p)
    
    def derivative(self,values,matrix):
        """Calculates the m-th derivateive of a function at barycentric nodes
        given by parameter values at barycentric nodes by means of a differentiation matrix
        
        Parameters:
        values (ndarray[nNodes]): values at sampling points
        matrix (ndarray[nNodes,nNodes]): m-th differentiation matrix 

        Returns:
        ndarray[nNoes] : values of the derivative function at the sampling points
        """
        
        
        #p'(s_i)=Sum_{j=0}^n l'_j(s_i)f_j
        p = np.dot(matrix,values)        
        return p
    
    def differentiationMatrix(self,m,nodes,weights,plot=False):
        """Calculates the m-th differentiation matrix for a function given at barycentric nodes 
        
        Parameters:
        m (int): m-th derivative of the given function
        nodes (ndarray[nNodes]): Gaus-Lobatto nodes
        weights (ndarray[nNodes]): barycentric weights for Gaus-Lobatto nodes

        Returns:
        ndarray[nNoes,nNodes] : m-th differentiation matrix
        """
        
        nNodes=len(nodes)
        #calculate some matrices frequenty used in the following calculation
        temp1=np.repeat(np.reshape(weights,(nNodes,1)),nNodes,axis=1)
        temp2=np.transpose(temp1)
        tempW = temp2/temp1 #w_j / w_i
        temp3=np.repeat(np.reshape(nodes,(nNodes,1)),nNodes,axis=1)
        temp4=np.transpose(temp3)
        tempS = temp3-temp4 #s_i - s_j

        #calculate matrix of first derivative
        temp5=tempW/tempS
        temp5[temp5==np.inf]=0
        temp6=-np.sum(temp5,axis=1)
        row,col = np.diag_indices(temp5.shape[0])
        temp5[row,col] = temp6

        if m==1:
            D = temp5
        elif m>1:
            for i in range(2,m+1):
                temp7 = np.repeat(np.reshape(np.diag(temp5),(nNodes,1)),nNodes,axis=1)
                temp5 = np.nan_to_num(i/tempS*(tempW*temp7-temp5))
                temp6=-np.sum(temp5,axis=1)
                row,col = np.diag_indices(temp5.shape[0])
                temp5[row,col] = temp6
            D = temp5
        else:
            raise Exception('degree of derivative not supported')
        
        if plot:
            plt.matshow(D)
            plt.colorbar()
            plt.show()
        
        return D