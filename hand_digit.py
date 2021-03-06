from sklearn import datasets
digits = datasets.load_digits()
import matplotlib.pyplot as plt

images_and_labels = list(zip(digits.images, digits.target))
plt.figure(figsize=(16,12),dpi=200)
for index, (image, label) in enumerate(images_and_labels[:8]):
	plt.subplot(2, 4, index+1)
	plt.axis('off')
	plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
	plt.title('Digit: %i' % label, fontsize = 10)
plt.show()
