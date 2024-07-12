from Bio.Seq import Seq

def check_cftr_mutations(protein_sequence):
    cftr_mutations = [
        
        ("F508del",  507, 'F',''),
        ("G542X", 541, 'G', 'X'),
        ("W1282X",  1281, 'W', 'X'),
        ("N1303K",  1302, 'N', 'K'),
        ("R117H",  116, 'R', 'H'),
        ("I507del", 506, 'I',''),
        ("S1251N",  1250, 'S', 'N'),
        ("A455E",  454, 'A', 'E'),
        ("G85E",  84, 'G', 'E'),
        ("Y1092X", 1091, 'Y', 'X'),
        ("R553X",  552, 'R', 'X'),
        ("G551D",  550, 'G', 'D'),
        ("W846X",  845, 'W', 'X'),
        ("S549R",  548, 'S', 'R'),
        ("R334W",  333, 'R', 'W')
        
    ]
    

    for mutation_name, position,actual_aa,expected_aa in cftr_mutations:
        if 'del' not in mutation_name:
            if protein_sequence[position] !=actual_aa and protein_sequence[position]==expected_aa:
                return True, mutation_name
        else:
            if protein_sequence[position] !=actual_aa:
                return True, mutation_name

    return False, None

def main():
   
    filename = r"E:\College\3rd SEM\INTELLIGENCE OF BIOLOGICAL SYSTEMS-1\PROJECT\sequencecftr.fasta"
    
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