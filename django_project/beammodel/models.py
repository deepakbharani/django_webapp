from django.db import models
#from matrix_field import MatrixField

class Beam(models.Model):
	# Mass Matrix
	mmatrix = models.TextField()
	# Stiffness Matrix
	smatrix = models.TextField()


	def __str__(self):
		return (self.mmatrix * self.smatrix)

