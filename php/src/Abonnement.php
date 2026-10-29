<?php
class Abonnement
{
    private string $titulaire;
    private string $formule;
    private bool $actif = true;

    private const PRIX = ['mensuel' => 45.0, 'annuel' => 450.0];

    public function __construct(string $titulaire, string $formule)
    {
        if (!array_key_exists($formule, self::PRIX)) {
            throw new InvalidArgumentException("Formule inconnue : $formule");
        }
        $this->titulaire = $titulaire;
        $this->formule = $formule;
    }

    public function getTitulaire(): string { return $this->titulaire; }
    public function getFormule(): string { return $this->formule; }
    public function prix(): float { return self::PRIX[$this->formule]; }
    public function estActif(): bool { return $this->actif; }

    public function suspendre(): void
    {
        if (!$this->actif) { throw new Exception("Déjà suspendu"); }
        $this->actif = false;
    }

    public function reactiver(): void
    {
        if ($this->actif) { throw new Exception("Déjà actif"); }
        $this->actif = true;
    }
}