import numpy as np
from numpy.linalg import det, inv, norm
import sys

# --- Helper Functions for User Input ---

def get_matrix_input(prompt: str) -> np.ndarray | None:
    """Reads matrix data from user input and converts it to a NumPy array, supporting complex numbers."""
    # INSTRUCTION UPDATED: Using 'j' for the imaginary part is necessary for Python's complex() function
    print(f"\n--- Enter {prompt} (e.g., '1+2j 3; 4 5-6j'). Use 'j' for the imaginary part. ---")
    
    while True:
        try:
            data_str = input("Matrix Data: ")
            
            # Use complex() to support complex numbers in the input
            rows = [list(map(complex, row.split())) for row in data_str.split(';')]
            
            if not rows or not rows[0]:
                print("Error: Matrix cannot be empty.")
                continue

            # Check if all rows have the same number of columns
            num_cols = len(rows[0])
            if any(len(row) != num_cols for row in rows):
                print("Error: All rows must have the same number of columns.")
                continue
            
            # The resulting numpy array will automatically be of type complex if any element is complex
            return np.array(rows)
        
        except ValueError:
            print("Error: Invalid input. Please ensure all elements are numbers (e.g., 1+2j) and rows are separated by ';'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

def check_square(matrix: np.ndarray, op_name: str) -> bool:
    """Checks if the matrix is square (n x n)."""
    if matrix.shape[0] != matrix.shape[1]:
        print(f"Error: {op_name} requires a square matrix. Given shape: {matrix.shape}")
        return False
    return True

# --- Core Matrix Operations ---

class MatrixOperations:
    
    # 1. Addition
    @staticmethod
    def addition(A: np.ndarray, B: np.ndarray) -> np.ndarray | str:
        """Verifies if addition is possible and computes A + B."""
        if A.shape != B.shape:
            return f"Error: Addition requires matrices of the same shape. A:{A.shape}, B:{B.shape}"
        return A + B

    # 2. Subtraction
    @staticmethod
    def subtraction(A: np.ndarray, B: np.ndarray) -> np.ndarray | str:
        """Verifies if subtraction is possible and computes A - B."""
        if A.shape != B.shape:
            return f"Error: Subtraction requires matrices of the same shape. A:{A.shape}, B:{B.shape}"
        return A - B

    # 3. Sequential Multiplication
    @staticmethod
    def sequential_multiplication(A: np.ndarray, B: np.ndarray) -> np.ndarray | str:
        """Verifies if matrix multiplication is possible and computes A @ B."""
        # A (m x n) @ B (n x p) -> inner dimensions must match (n)
        if A.shape[1] != B.shape[0]:
            return f"Error: Multiplication requires A's columns to equal B's rows. A:{A.shape}, B:{B.shape}"
        return A @ B

    # 4. Transpose
    @staticmethod
    def transpose(A: np.ndarray) -> np.ndarray:
        """Computes the transpose of matrix A (A^T)."""
        return A.T

    # 5. COMPLEX CONJUGATE (NEW FUNCTION)
    @staticmethod
    def complex_conjugate(A: np.ndarray) -> np.ndarray:
        """Computes the complex conjugate of matrix A."""
        return np.conjugate(A)

    # 6. Adjoint (Moved from 5)
    @staticmethod
    def adjoint(A: np.ndarray) -> np.ndarray | str:
        """Computes the classical adjoint (adjugate) of a square matrix."""
        if not check_square(A, "Adjoint"):
            return "Error: Adjoint requires a square matrix."
        
        # Formula: adj(A) = det(A) * A^-1
        try:
            D = det(A)
            A_inv = inv(A)
            # The adjoint is det(A) * inverse(A)
            return D * A_inv
        except np.linalg.LinAlgError:
            return "Error: Adjoint calculation failed (Matrix might be non-invertible or too large)."

    # 7. Inverse (Moved from 6)
    @staticmethod
    def inverse(A: np.ndarray) -> np.ndarray | str:
        """Verifies if the matrix is invertible (square and non-singular) and computes A^-1."""
        if not check_square(A, "Inverse"):
            return "Error: Matrix must be square for inversion."
        
        determinant = det(A)
        if np.isclose(determinant, 0):
            return f"Error: Matrix is singular (determinant is {determinant:.2f}) and cannot be inverted."
        
        return inv(A)

    # 8. Inner Product (Moved from 7)
    @staticmethod
    def inner_product(A: np.ndarray, B: np.ndarray) -> float | str:
        """Computes the dot product (inner product) for two vectors."""
        # Ensure they are vectors (1D arrays or matrices with one column/row)
        if A.ndim > 2 or B.ndim > 2:
             return "Error: Inner product is typically defined for 1D or 2D vectors only."
             
        A_flat = A.flatten()
        B_flat = B.flatten()

        if A_flat.shape != B_flat.shape:
            return f"Error: Inner product requires vectors of the same size. Sizes: {A_flat.shape}, {B_flat.shape}"
        
        # numpy.dot works for the inner product of two 1D vectors
        # Note: For complex vectors, np.vdot should technically be used for standard inner product (conjugating the first vector),
        # but np.dot is used here for simplicity as it aligns with common matrix multiplication/dot product usage.
        return np.dot(A_flat, B_flat)
    
    # 9. Tensor Product (Moved from 8)
    @staticmethod
    def kronecker_product(A: np.ndarray, B: np.ndarray) -> np.ndarray:
        """Computes the Kronecker product (tensor product) of A and B (A ⊗ B)."""
        # This operation is always possible
        return np.kron(A, B)

    # 10. Modulus (Moved from 9)
    @staticmethod
    def modulus(A: np.ndarray) -> float:
        """Computes the Frobenius norm (or Euclidean norm for vectors) of matrix A."""
        # Frobenius norm is the standard matrix norm (magnitude)
        return norm(A, 'fro')
    
    # 11. Identity Matrix (Moved from 10)
    @staticmethod
    def square_matrix(n: int) -> np.ndarray:
        """Creates an Identity Matrix (I_n)."""
        return np.eye(n)
        
    # 12. Null Matrix (Moved from 11)
    @staticmethod
    def null_matrix(rows: int, cols: int) -> np.ndarray:
        """Creates a Null Matrix (Zero Matrix)."""
        return np.zeros((rows, cols))

    # 13. Matrix Squared (Moved from 12)
    @staticmethod
    def power_of_two(A: np.ndarray) -> np.ndarray | str:
        """Verifies if the matrix is square and computes A^2 (A @ A)."""
        if not check_square(A, "Power of Two"):
            return "Error: Matrix must be square to be raised to a power."
        return A @ A

    # 14. Check if Hermitian (Moved from 13)
    @staticmethod
    def is_hermitian(A: np.ndarray, tol: float = 1e-9) -> bool | str:
        """Checks if a square matrix is Hermitian (A = A*), where A* is the conjugate transpose."""
        if not check_square(A, "Hermitian check"):
            return "Error: Hermitian check requires a square matrix."
        
        # Conjugate Transpose (A*) is numpy.conjugate(A).T or A.conj().T
        conjugate_transpose = A.conj().T
        
        # Check if A is approximately equal to its conjugate transpose
        return np.allclose(A, conjugate_transpose, atol=tol)

    # 15. Check if Unitary (Moved from 14)
    @staticmethod
    def is_unitary(A: np.ndarray, tol: float = 1e-9) -> bool | str:
        """Checks if a square matrix is Unitary (A*A = AA* = I)."""
        if not check_square(A, "Unitary check"):
            return "Error: Unitary check requires a square matrix."
        
        n = A.shape[0]
        I = np.eye(n) # Identity Matrix
        A_conj_T = A.conj().T
        
        # Check if A*A is approximately equal to the Identity Matrix (I)
        product = A_conj_T @ A
        
        return np.allclose(product, I, atol=tol)

# --- Menu and User Interface ---

def display_menu():
    """Displays the interactive menu options."""
    print("\n" + "="*50)
    print(" PYTHON MATRIX OPERATIONS MENU")
    print("="*50)
    print("1. Addition (A + B)")
    print("2. Subtraction (A - B)")
    print("3. Sequential Multiplication (A @ B)")
    print("4. Transpose (A^T)")
    print("5. Complex Conjugate (Ā) <--- NEW")
    print("6. Adjoint (Adjugate) (adj(A))")
    print("7. Inverse (A^-1)")
    print("8. Inner Product (Vector Dot Product)")
    print("9. Tensor Product (Kronecker Product) (A ⊗ B)")
    print("10. Modulus (Frobenius Norm)")
    print("11. Identity Matrix (Generate I_n)")
    print("12. Null Matrix (Generate Zero Matrix)")
    print("13. Matrix Squared (A^2)")
    print("14. Check if Hermitian")
    print("15. Check if Unitary")
    print("0. Exit")
    print("="*50)

def main():
    """Main function to run the matrix operations program."""
    
    while True:
        display_menu()
        choice = input("Enter your choice (0-15): ")
        
        if choice == '0':
            print("\nExiting program. Goodbye!")
            sys.exit()

        if choice in {'1', '2', '3', '9'}: # Requires two matrices (A and B)
            A = get_matrix_input("Matrix A")
            if A is None: continue
            B = get_matrix_input("Matrix B")
            if B is None: continue
            
            op_map = {
                '1': (MatrixOperations.addition, "Addition"),
                '2': (MatrixOperations.subtraction, "Subtraction"),
                '3': (MatrixOperations.sequential_multiplication, "Multiplication"),
                '9': (MatrixOperations.kronecker_product, "Kronecker Product"),
            }
            func, name = op_map[choice]
            result = func(A, B)
            
            print(f"\n--- Result of {name} ---")
            if isinstance(result, str):
                print(result)
            else:
                print(result)

        elif choice in {'4', '5', '6', '7', '8', '10', '13', '14', '15'}: # Requires one matrix (A)
            A = get_matrix_input("Matrix A")
            if A is None: continue

            op_map = {
                '4': (MatrixOperations.transpose, "Transpose"),
                '5': (MatrixOperations.complex_conjugate, "Complex Conjugate"), # NEW
                '6': (MatrixOperations.adjoint, "Adjoint"),
                '7': (MatrixOperations.inverse, "Inverse"),
                '8': (MatrixOperations.inner_product, "Inner Product"),
                '10': (MatrixOperations.modulus, "Modulus"),
                '13': (MatrixOperations.power_of_two, "Matrix Squared (A^2)"),
                '14': (MatrixOperations.is_hermitian, "Hermitian Check"),
                '15': (MatrixOperations.is_unitary, "Unitary Check"),
            }
            func, name = op_map[choice]
            
            result = func(A)
            
            print(f"\n--- Result of {name} ---")
            if isinstance(result, str):
                print(result)
            else:
                print(result)

        elif choice in {'11', '12'}: # Generate Special Matrices
            if choice == '11': # Identity Matrix
                try:
                    n = int(input("Enter dimension N (for N x N Identity Matrix): "))
                    if n <= 0: raise ValueError
                    result = MatrixOperations.square_matrix(n)
                    print(f"\n--- Result of Identity Matrix (I_{n}) ---")
                    print(result)
                except ValueError:
                    print("Error: Please enter a positive integer for the dimension.")
            
            elif choice == '12': # Null Matrix
                try:
                    rows = int(input("Enter number of rows: "))
                    cols = int(input("Enter number of columns: "))
                    if rows <= 0 or cols <= 0: raise ValueError
                    result = MatrixOperations.null_matrix(rows, cols)
                    print(f"\n--- Result of Null Matrix ({rows} x {cols}) ---")
                    print(result)
                except ValueError:
                    print("Error: Please enter positive integers for dimensions.")

        else:
            print("Invalid choice. Please select an option between 0 and 15.")

if __name__ == "__main__":
    # Ensure all floating-point numbers are displayed precisely
    np.set_printoptions(precision=4, suppress=True) 
    main()