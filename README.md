# Assignment1
Assigmnent 1 part 1 
group123 Atle Aaserød, Trym Dullum and Daniel Nygård

# Assignment-2

1. Pick one use case (defined below).
-  Vi valgte predict stock market price for TESLA.
2. Explore and research which algorithm would work best for this use case (regression or classification)
- Vi mener regression passer best for vår oppgave da denne formen er best for priser osv.
3. Document your findings in a file (3-5 lines) on why you chose this algorithm.
- Vi tenkte å bruke LSTM men denne ville ikke fungere(forklart nederst i teksten). Vi endte da med å bruke lineær regreson. 
4. Train the algorithm using Python
-  Vedlegg
5. Keep the solution as simple as possible. We are not looking for the best machine learning algorithm. We are interested in seeing that you know how to work with machine learning.
-  Vedlegg

group 123 Atle Aaserød, Trym Dullum and Daniel Nygård

Vi begynte med å bruke Long Short Term Memory (LSTM) men der fikk vi store problemer med å bruke både NumPy og Tensor. Numpy klarte ikke å lese symoblic tensor så da endte vi opp med å bruke en modifisert versjon av lab 4. 

Endte alltid opp med denne feilkoden. Etter mye leting virker det som det er probleremer med nyeste versjon av NumPy
NotImplementedError: Cannot convert a symbolic Tensor (lstm_15/strided_slice:0) to a numpy array. This error may indicate that you're trying to pass a Tensor to a NumPy call, which is not supported

Grunnleggende handler klassifisering om å forutsi en etikett og regresjon handler om å forutsi en mengde.
