class Solution(object):
    def removeSubfolders(self, folders):
        folders.sort()  # Trie les dossiers pour s'assurer que les parents viennent en premier
        result = []  # Liste des dossiers principaux

        for folder in folders:
            if not result or not folder.startswith(result[-1] + "/"):  
                result.append(folder)  # Ajoute le dossier s'il n'est pas un sous-dossier
        
        return result
