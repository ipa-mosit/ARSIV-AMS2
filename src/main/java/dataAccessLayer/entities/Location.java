package dataAccessLayer.entities;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;

@Entity
public class Location{
    @Id
    int id;
    int unit;
    int shelf;
    @ManyToOne
    @JoinColumn(name="halfCabinet_id")
    HalfCabinet halfCabinet;
}
