from sklearn.preprocessing import StandardScaler

class Logistic_Regression():
    def __init__(self, learning_rate, no_of_iterations):
        self.learning_rate = learning_rate
        self.no_of_iterations = no_of_iterations
        self.cost_history = []   # Store loss values for visualization

    def fit(self, X, Y):
        # Store dimensions of training data
        self.m, self.n = X.shape
        # Initialize weights and bias
        self.w = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.Y = Y

        # Scale features for stability
        scaler = StandardScaler()
        self.X = scaler.fit_transform(self.X)

        # Gradient descent loop
        for i in range(self.no_of_iterations):
            self.update_weights()
            if (i % (self.no_of_iterations/10) == 0):
                print(f"Iteration: {i}")

    def update_weights(self):
        # Sigmoid function
        Y_hat = 1 / (1 + np.exp(-(self.X.dot(self.w) + self.b)))

        # Compute cost and save it
        cost = -np.mean(self.Y * np.log(Y_hat) + (1 - self.Y) * np.log(1 - Y_hat))
        self.cost_history.append(cost)

        # Compute gradients
        dw = (1 / self.m) * np.dot(self.X.T, (Y_hat - self.Y))
        db = (1 / self.m) * np.sum(Y_hat - self.Y)

        # Update weights & bias
        self.w = self.w - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db

    def predict(self, X):
        # Scale test data
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
        # Prediction using sigmoid
        Y_pred = 1 / (1 + np.exp(-(X.dot(self.w) + self.b)))
        Y_pred = np.where(Y_pred > 0.5, 1, 0)   # Convert probabilities to 0/1
        return Y_pred