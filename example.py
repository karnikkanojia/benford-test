from benfordslaw import benfordslaw

# Initialize
bl = benfordslaw(alpha=0.05)

# Load elections example
df = bl.import_example(data='RUS')

# Extract election information.
X = df['votes'].values

# Print
print(X)
# array([ 5387, 23618,  1710, ...,    16,    21,     0], dtype=int64)

# Make fit
results = bl.fit(X)

# Plot
bl.plot(title='Donald Trump')