// Use this example job configuration file as a starting point for your own
// files.
{
  seed: 123456, // Random number seed (omit to use time since Unix epoch)

  // Pure 40Ar target
  target: { 					//determines what's in detector
    nuclides: [ 1000180400 ],
    atom_fractions: [ 1.0 ],
  },

  // Simulate CC ve scattering on 40Ar
  reactions: [ "ve40ArCC_Bhattacharya2009.react", "ES.react", "CEvNS40Ar.react" ], //what reactions im interested In observing
// listing both types of ES scattering so the computer will just pick which one corresponds w the data

  // Neutrino source specification // determining energy distribution. Of incoming neutrinos
  source: {
    type: "fermi-dirac", // energy of cosmic neutrino bkgd follows shape of fermi-dirac curve
    neutrino: "ve",       // The source produces electron neutrinos
    Emin: 0,              // Minimum neutrino energy (MeV)
    Emax: 60,             // Maximum neutrino energy (MeV)
    temperature: 10,     // Temperature (MeV)
    eta: 6.5                // Pinching parameter (dimensionless, default 0) 
	// eta takes a distribution and makes it more peaked if u want it
  },

  // Incident neutrino direction 3-vector
  direction: { x: 0.0, y: 0.0, z: 1.0 },

  // Settings for marley command-line executable
  executable_settings: {

    // The number of events to generate
    events: 3000,

    // Event output configuration
    output: [ { file: "proneutr_star.ascii", format: "ascii", mode: "overwrite" } ], 
//where to save output file

  },
}
