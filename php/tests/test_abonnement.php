<?php
$a = new Abonnement('Sara', 'mensuel');
verifier($a->estActif(), 'Un nouvel abonnement est actif');
verifier($a->prix() === 45.0, 'Le prix mensuel est 45.0');
$a->suspendre();
verifier(!$a->estActif(), 'Après suspension, il est inactif');

try { $a->suspendre(); verifier(false, 'Double suspension refusée'); }
catch (Exception $e) { verifier(true, 'Double suspension refusée'); }

$a->reactiver();
verifier($a->estActif(), 'Après réactivation, il est actif');

try { new Abonnement('Sara', 'hebdo'); verifier(false, 'Formule inconnue refusée'); }
catch (InvalidArgumentException $e) { verifier(true, 'Formule inconnue refusée'); }