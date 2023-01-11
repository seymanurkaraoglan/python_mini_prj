import pikepdf

old_pdf = pikepdf.Pdf.open("the path to the pdf you want to encrypt")

no_extr = pikepdf.Permissions(extract=False)

old_pdf.save("the path of encrypted pdf with new name",
            encryption=pikepdf.Encryption(user="any password you want",
                                          owner="owner name",
                                          allow=no_extr))