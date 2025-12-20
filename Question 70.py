# Q. Create a class Book with the following attributes:
# • title
# • author
# • list of reviews 

# And add methods to:
# • add a new review
# • count reviews
# • display all reviews


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.list_of_reviews = []

    def add_new_reviews(self, reviews):
        self.list_of_reviews.append(reviews)

    def count_reviews(self):
        print("Count Reviews: ",len(self.list_of_reviews))

    def display_all_reviews(self):
        if len (self.list_of_reviews) == 0:
            print("No reviews")
        else:
            print("reviews: ")
            for r in self.list_of_reviews:
                print(r)

b = Book("Harry Potter", "J.K. Rowling")
b.add_new_reviews(["Mysterious Book", "High Much Rated", "Good for education purposes"])

print("Count Reviews:", b.count_reviews())
b.display_all_reviews()