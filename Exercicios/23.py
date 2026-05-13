def filtrar(lista, dominio):
    lista_email = []
    for email in lista:
        if dominio in email:
            lista_email.append(email)
    for novo in lista_email:
        print(novo)

emails = ["joao.silva@gmail.com", "maria.oliveira@hotmail.com", "carlos.souza@yahoo.com", "ana.costa@outlook.com",
          "pedro.lima@gmail.com", "juliana.alves@hotmail.com", "rafael.pereira@yahoo.com", "fernanda.rocha@icloud.com",
          "lucas.martins@gmail.com", "camila.gomes@hotmail.com", "bruno.ribeiro@yahoo.com", "patricia.melo@outlook.com",
          "diego.barbosa@gmail.com", "aline.cardoso@hotmail.com", "marcos.teixeira@yahoo.com",
          "beatriz.araujo@icloud.com", "thiago.nunes@gmail.com", "renata.freitas@hotmail.com",
          "gustavo.moura@yahoo.com", "larissa.vieira@outlook.com", "eduardo.farias@gmail.com",
          "priscila.dias@hotmail.com", "vinicius.cunha@yahoo.com", "tatiane.borges@icloud.com",
          "felipe.torres@gmail.com", "simone.campos@hotmail.com", "andre.batista@yahoo.com",
          "paula.rezende@outlook.com", "rodrigo.macedo@gmail.com", "debora.pinto@hotmail.com",
          "leandro.monteiro@yahoo.com", "elaine.ramos@icloud.com", "fabio.carvalho@gmail.com",
          "cristiane.lopes@hotmail.com", "henrique.ferreira@yahoo.com", "monica.garcia@outlook.com",
          "daniel.andrade@gmail.com", "sandra.peixoto@hotmail.com", "ricardo.neves@yahoo.com",
          "carla.machado@icloud.com", "alexandre.correia@gmail.com", "viviane.miranda@hotmail.com",
          "paulo.sergio@yahoo.com", "regina.santos@outlook.com", "mateus.leite@gmail.com", "claudia.assis@hotmail.com",
          "caio.duarte@yahoo.com", "suelen.azevedo@icloud.com", "igor.moreira@gmail.com", "daniela.porto@hotmail.com",
          "adriano.brito@yahoo.com", "mariana.tavares@outlook.com", "jorge.nascimento@gmail.com",
          "flavia.coelho@hotmail.com", "wesley.pacheco@yahoo.com", "isabela.fonseca@icloud.com",
          "renan.cesar@gmail.com", "bianca.valente@hotmail.com", "samuel.paiva@yahoo.com",
          "gabriela.queiroz@outlook.com", "arthur.mendes@gmail.com", "aline.fernandes@hotmail.com",
          "murilo.guedes@yahoo.com", "luciana.prado@icloud.com", "victor.sampaio@gmail.com",
          "jessica.barbieri@hotmail.com", "otavio.rangel@yahoo.com", "karina.nogueira@outlook.com",
          "raul.bittencourt@gmail.com", "amanda.ventura@hotmail.com", "elio.moraes@yahoo.com",
          "natalia.cabral@icloud.com", "sergio.furtado@gmail.com", "fabiana.lacerda@hotmail.com",
          "nilton.aguiar@yahoo.com", "brenda.esteves@outlook.com", "yuri.magalhaes@gmail.com",
          "tania.medeiros@hotmail.com", "vagner.pontes@yahoo.com", "heloisa.castro@icloud.com",
          "cesar.amaral@gmail.com", "silvia.antunes@hotmail.com", "jonas.veloso@yahoo.com",
          "raquel.almeida@outlook.com", "allan.cavalcante@gmail.com", "danubia.matias@hotmail.com",
          "kleber.ferraz@yahoo.com", "michele.dorneles@icloud.com", "evandro.pires@gmail.com",
          "paloma.assis@hotmail.com", "fabiano.dantas@yahoo.com", "joice.barreto@outlook.com",
          "tiago.beltrao@gmail.com", "geovana.muniz@hotmail.com", "hugo.siqueira@yahoo.com",
          "valeria.fagundes@icloud.com", "ismael.alcantara@gmail.com", "rosana.cunha@hotmail.com",
          "luiz.otero@yahoo.com", "cintia.marques@outlook.com", "roberta.alencar@gmail.com",
          "emanuel.galvao@hotmail.com", "tatiana.vargas@yahoo.com", "paulo.lemos@icloud.com"]


verificar = filtrar(emails, '@yahoo.com', )


