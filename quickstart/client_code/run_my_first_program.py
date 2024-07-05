from nada_dsl import *

def nada_main():

    # Define parties involved
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Input integers from both parties
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party2))

    # Perform addition operation on the secret integers
    new_int = my_int1 + my_int2

    # Output the result to both parties
    return [Output(new_int, "my_output_party1", party1), 
            Output(new_int, "my_output_party2", party2)]

# Instantiate the program
nada_main()
