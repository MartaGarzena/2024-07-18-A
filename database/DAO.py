from database.DB_connect import DBConnect
from model.gene import Gene
from model.interaction import Interaction


class DAO():

    @staticmethod
    def get_all_genes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                    FROM genes"""
            cursor.execute(query)

            for row in cursor:
                result.append(Gene(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_interactions():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                       FROM interactions"""
            cursor.execute(query)

            for row in cursor:
                result.append(Interaction(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_Chromosoma():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct Chromosome  as N
            from genes g 
            order by N"""
            cursor.execute(query)

            for row in cursor:
                result.append(row["N"])

            cursor.close()
            cnx.close()
        return result
    ''' @staticmethod
    def haveInteraction():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ select c1.GeneID as c1, c2.GeneID as c2
                        from classification c1, classification  c2
                        where c1.Localization = c2.Localization """
            cursor.execute(query,)

            for row in cursor:
                result.append((row["c1"], row["c2"]))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def haveLocalizzazione(genId1, genId2):
        cnx = DBConnect.get_connection()
        result = None
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """ select count(*) as bu, i.Expression_Corr as peso
                        from  interactions i 
                        where i.GeneID1 = %s
                        and i.GeneID2 = %s
                        """
            cursor.execute(query, (genId1, genId2,))

            for row in cursor:
                if row["bu"] != 0:
                    result = row["peso"]

            cursor.close()
            cnx.close()
        return result
    '''

    @staticmethod
    def getArchi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select g.GeneID as g1, g.function as f1, g2.GeneID as g2, g2.function as f2 ,i.Expression_Corr as peso 
                    from genes_small.interactions i
                    left join genes_small.classification c on i.GeneID1=c.GeneID
                    left join genes_small.genes g on i.GeneID1 = g.geneID
                    left join genes_small.classification c2 on i.GeneID2 =c2.GeneID
                    left join genes_small.genes g2 on i.GeneID2 = g2.geneID 
                    where c.Localization=c2.Localization   """
            cursor.execute(query, )

            for row in cursor:
                result.append((row["g1"], row["f1"], row["g2"],row["f2"], row["peso"]))

            cursor.close()
            cnx.close()
        return result




