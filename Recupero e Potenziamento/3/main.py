from ReP3_D_Candido import *

if __name__ == "__main__":
    a = Alieno("Alieno", 0)  # il nome sarà corretto automaticamente
    m = Mostro("gorthor", "GRAAAHHH", "uuurgghh...", [])

    m.setAssalto()

    print(a)
    print()
    print(m)
    print("\nCombattimento\n")

    vincitore = combattimento(a, m)

    print(proclamaVincitore(vincitore))
