def freelancer():

   horas_estimadas =float(input("informe as horas estimadas:")) 
   valor_hora =float(input("informe o valor por hora:"))
   valor_inicial =int(input("informe o valor inicial:")) 
   taxa =float(input("informe a taxa inicial:"))

   valor_taxa = (horas_estimadas * valor_hora + valor_inicial) * taxa / 100
   valor_total = valor_taxa + valor_inicial + horas_estimadas * valor_hora

   print(f"{valor_taxa:.2f}")

   print(f"{valor_total:.2f}")

freelancer()