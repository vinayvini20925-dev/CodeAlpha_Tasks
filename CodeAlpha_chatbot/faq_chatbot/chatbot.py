faq_data = [
    ("What is your return policy?", "You can return items within 30 days."),
    ("How do I track my order?", "Use the tracking link sent to your email."),
    ("Do you offer customer support?", "Yes, 24/7 via chat and email."),
    ("Where are you located?", "We are an online store."),
    ("What payment methods do you accept?", "We accept credit cards and PayPal."),
    ("What are your business hours?", "Our services are available 24/7 online."),
    ("Do you offer refunds?", "Yes, we offer refunds according to our refund policy."),
    ("What are your business hours?", "Our services are available 24/7 online."),
    ("Do you offer refunds?", "Yes, we offer refunds according to our refund policy."),
    ("How can I contact support?", "You can contact us through chat or email support."),
    ("Do you provide international shipping?", "Yes, we ship to many countries worldwide."),
    ("How long does delivery take?", "Delivery usually takes 3-7 business days."),
    ("Can I track my order?", "Yes, you will receive a tracking link after your order is shipped."), 
    ("Do you offer discounts?", "Yes, we occasionally offer discounts and promotional offers."),
    ("Is my payment information secure?", "Yes, all payments are processed through secure systems."),
    ("Can I cancel my order?", "Yes, orders can be canceled before they are shipped."),
    ("Do you have a return policy?", "Yes, we have a 30-day return policy."),
    ("How can I create an account?", "You can create an account by signing up on our website."),
    ("Do I need an account to place an order?", "No, you can place an order as a guest."),
    ("How can I reset my password?", "Click on 'Forgot Password' on the login page."),
    ("Do you offer cash on delivery?", "Currently we only accept online payments."),
    ("Are there any delivery charges?", "Delivery charges depend on your location."),
    ("How can I change my order?", "You can modify your order before it is shipped."),
    ("How will I know if my order is confirmed?", "You will receive a confirmation email."),
    ("Can I update my delivery address?", "Yes, you can update it before the order is shipped."),
    ("What should I do if my order is delayed?", "Please contact our support team for help."),
    ("Do you offer gift cards?", "Yes, we offer digital gift cards."),
    ("Can I order products in bulk?", "Yes, please contact our sales team for bulk orders."),
    ("Do you have a mobile app?", "Yes, our mobile app is available on Android and iOS."),
    ("How can I give feedback?", "You can send feedback through our contact page."),
    ("Do you provide customer service on weekends?", "Yes, our support is available 24/7."),
    ("How do I delete my account?", "Please contact customer support to delete your account."),
    ("What happens if my payment fails?", "You can try the payment again or use another method."),
    ("Is there a warranty on products?", "Yes, warranty depends on the product."),
    ("How can I subscribe to your newsletter?", "You can subscribe using the form on our website."),
    ("How do I check product availability?", "Product availability is shown on the product page.")
]

import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('punkt_tab')

def preprocess(text):
    text = text.lower()  # lowercase
    text = "".join([char for char in text if char not in string.punctuation])  # remove punctuation
    tokens = nltk.word_tokenize(text)  # tokenize
    return " ".join(tokens)

questions = [preprocess(q) for q, a in faq_data]
answers = [a for q, a in faq_data]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_answer(user_input):
    user_input = preprocess(user_input)
    user_vec = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vec, X)
    score = similarity.max()
    index = similarity.argmax()
    max_similarity = similarity[0][index]
    print("Similarity:",max_similarity)

    if max_similarity < 0.6:

        return "Sorry, I don't understand."

    return answers[index]

print("Chatbot: Hello! Ask me something (type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = get_answer(user_input)
    print("Chatbot:", response)