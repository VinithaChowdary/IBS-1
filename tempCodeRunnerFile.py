ilename = r"E:\College\3rd SEM\INTELLIGENCE OF BIOLOGICAL SYSTEMS-1\PROJECT\sequencecftr.fasta"
    
    try:
        with open(filename, 'r') as file:
            protein_sequence = file.read().strip()
        
        seq_obj = Seq(protein_sequence)
        
        has_mutation, mutation = check_cftr_mutations(seq_obj)
        
        if has_mutation:
            print(f"Diagnosed with cystic fibrosis with {mutation} mutation.")
        else:
            print("Not diagnosed with cystic fibrosis.")
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()